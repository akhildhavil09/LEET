class Solution(object):
    def partition(self, s):
        res=[]
        path=[]
        def palinhelper(index):
            if index==len(s):
                res.append(path[:])
                return
            for i in range(index,len(s)):
                if ispalin(s,index,i):
                    path.append(s[index:i+1])
                    palinhelper(i+1)
                    path.pop()
        def ispalin(s,start,end):
            while start<= end:
                if s[start]!=s[end]:
                    return False
                start+=1
                end-=1
            return True
        palinhelper(0)
        return res
        