class Solution(object):
    def rob(self, nums):
        return max(nums[0],self.helper(nums[1:]),self.helper(nums[:-1]))

    def helper(self,nums):
        rob1,rob2=0,0
        for i in nums:
            current=max(rob1+i,rob2)
            rob1=rob2
            rob2=current
        return rob2
        