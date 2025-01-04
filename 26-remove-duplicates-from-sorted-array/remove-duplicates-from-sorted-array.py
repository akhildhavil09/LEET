class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        index=0

        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            nums[index]=nums[i]
            index+=1
        return index