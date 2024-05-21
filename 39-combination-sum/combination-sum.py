class Solution(object):
    def combinationSum(self, can, target):
        can.sort()
        res=[]
        def backtrack(start, target, cur_subset, res):
            if target==0:
                res.append(cur_subset[:])
            for i in range(start, len(can)):
                if can[i]>target:
                    break
                cur_subset.append(can[i])
                backtrack(i, target-can[i],cur_subset,res)
                cur_subset.pop()
        backtrack(0,target,[],res)
        return res
        