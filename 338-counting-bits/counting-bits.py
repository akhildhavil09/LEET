class Solution(object):
    def countBits(self, n):
        res=[]
        for i in range(0,n+1):
            count=0
            for j in bin(i):
                if j=="1": count+=1
            res.append(count)
        return res
        