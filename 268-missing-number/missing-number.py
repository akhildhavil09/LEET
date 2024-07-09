class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        esum=n*(n+1) //2
        sums= sum(nums)
        return esum-sums