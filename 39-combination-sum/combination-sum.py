class Solution(object):
    def combinationSum(self, nums, target):
        res=[]
        sub=[]

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
