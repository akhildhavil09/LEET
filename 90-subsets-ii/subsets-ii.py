class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        
        def f(index,cur):
            if index==len(nums):
                res.append(cur[::])
                return
            
            cur.append(nums[index])
            f(index+1,cur)
            cur.pop()

            while index+1<len(nums) and nums[index]==nums[index+1]:
                index+=1
            f(index+1,cur)
        f(0,[])

        return res
            