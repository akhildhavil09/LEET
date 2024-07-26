class Solution(object):
    def subsets(self, nums):
        res=[]
        def dfs(start,subset):
            res.append(subset)
            for i in range(start, len(nums)):
                subset.append(nums[i])
                dfs(i+1, subset)
                subset.pop()
        dfs(0,[])
        return res
        