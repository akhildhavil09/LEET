class Solution(object):
    def removeElement(self, nums, val):
        w=0
        for r in range(len(nums)):
            if nums[r]!=val:
                nums[w],nums[r]= nums[r], nums[w]
                w+=1
        return w
        