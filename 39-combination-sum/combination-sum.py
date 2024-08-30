class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sub=[]
        res=[]

        def dfs(index):
            if sum(sub)==target:
                res.append(sub[:])
                return
            
            if sum(sub)>target or index>=len(nums):
                return

            sub.append(nums[index])
            dfs(index)
            sub.pop()
            dfs(index+1)

        dfs(0)
        return res