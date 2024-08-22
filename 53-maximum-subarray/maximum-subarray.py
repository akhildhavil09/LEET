class Solution(object):
    def maxSubArray(self, nums):
        if len(nums)==0: return 0
        max_cur=max_global= nums[0]

        for num in nums[1:]:
            max_cur=max(num,max_cur+num)
            
            max_global= max(max_global, max_cur)

        return max_global        