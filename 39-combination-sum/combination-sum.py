class Solution(object):
    def combinationSum(self, candi, target):
        candi.sort()
        result=[]
        def dfs(start, target, cursub, result):
            if target==0:
                result.append(cursub[:])
                return
            for i in range(start, len(candi)):
                if candi[i] > target:
                    break
                cursub.append(candi[i])
                dfs(i, target-candi[i],cursub,result)
                cursub.pop()
        dfs(0,target,[],result)
        return result