class Solution(object):
    def partition(self, s):
        def palin(sub):
            return sub==sub[::-1]
        def parti(start,path):
            if start==len(s):
                res.append(path[:])
                return
            
            for end in range(start, len(s)):
                substring= s[start:end+1]
                if palin(substring):
                    path.append(substring)
                    parti(end+1,path)
                    path.pop()
        res=[]
        parti(0,[])
        return res
        