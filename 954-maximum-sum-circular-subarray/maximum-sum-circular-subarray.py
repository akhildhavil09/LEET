class Solution(object):
    def maxSubarraySumCircular(self, nums):
        def kadane(nums):
            cur_max= max_global= nums[0]
            for num in nums[1:]:
                cur_max= max(num, cur_max+num)

                max_global= max( max_global, cur_max)
            return max_global
        # step1: without wraparound
        max_kadane= kadane(nums)

        #step2: with wraparound
        total_sum= sum(nums)
        min_kadane=kadane([-num for num in nums])

        max_wraparound= total_sum+min_kadane

        #step3: compare the 2 cases

        if max_wraparound==0:
            return max_kadane
        return max(max_kadane, max_wraparound)



        