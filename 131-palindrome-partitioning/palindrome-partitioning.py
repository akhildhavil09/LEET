class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        path=[]
        def ispalin(s,start,end):
            while start<=end:
                if s[start]!=s[end]:
                    return False
                start+=1
                end-=1
            return True

        def helper(index):
            if index==len(s):
                res.append(path[:])
                return
            for i in range(index,len(s)):
                if ispalin(s,index,i):
                    path.append(s[index:i+1])
                    helper(i+1)
                    path.pop()
        helper(0)
        return res
                