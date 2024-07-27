class Solution(object):
    def permute(self, nums):
        res=[]
        def dfs(cur,remains):
            if not remains:
                res.append(cur[:])
                return
            for i in range(len(remains)):
                cur.append(remains[i])
                dfs(cur,remains[:i]+remains[i+1:])
                cur.pop()
        dfs([],nums)
        return res
        