class Solution(object):
    def rob(self, nums):
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
    def helper(self,nums):
        rob1,rob2=0,0
        for n in nums:
            current_rob= max(n+rob1, rob2)
            rob1=rob2
            rob2=current_rob
        return rob2