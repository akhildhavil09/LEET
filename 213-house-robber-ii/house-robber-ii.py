class Solution:
    def robLinear(self, nums):
        n=len(nums)
        if n==0:
            return 0
        if n==1:
            return nums[0]

        dp=[0]*n
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])

        for i in range(2,n):
            dp[i]=max(dp[i-1],dp[i-2]+nums[i])
        
        return dp[-1]

    def rob(self,nums):
        n=len(nums)
        if n==0: return 0
        if n==1: return nums[0]

        #case1: Include first house, resulting cant include last house
        case1= self.robLinear(nums[:-1])

        #case2: Start from 2nd house, end at last house
        case2= self.robLinear(nums[1:])

        return max(case1,case2)
    
        