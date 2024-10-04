class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res=[-1,-1]
        for i in range(len(nums)):
            if nums[i]==target:
                res[0]=i
                break
        for j in range(len(nums)-1,-1,-1):
            if nums[j]==target:
                res[1]=j
                break
        
        return res