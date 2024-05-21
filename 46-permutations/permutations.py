class Solution(object):
    def permute(self, nums):
        res=[]
        def dfs(cur, remain):
            if not remain: 
                res.append(cur[:])
                return
            for i in range(len(remain)):
                cur.append(remain[i])
                dfs(cur, remain[:i]+remain[i+1:])
                cur.pop()
        dfs([],nums)
        return res
        