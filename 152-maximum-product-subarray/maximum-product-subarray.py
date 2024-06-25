class Solution(object):
    def maxProduct(self, nums):
        res=max(nums)
        curmin,curmax=1,1
        for n in nums:
            if n==0:
                curmin,curmax=1,1
                continue
            tmp=curmax
            curmax=max(n*curmin,n*curmax,n)
            curmin=min(n*curmin,n*tmp,n)

            res=max(res,curmax)
        return res
        