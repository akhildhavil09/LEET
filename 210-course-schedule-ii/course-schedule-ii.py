class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        prehash={i:[] for  i in range(numCourses)}
        for crs,pre in prerequisites:
            prehash[crs].append(pre)
        state=[0]*numCourses
        res=[]
        def dfs(crs):
            if state[crs]==1: return False
            if state[crs]==2: return True
            state[crs]=1
            for pre in prehash[crs]:
                if not dfs(pre):
                    return False
            state[crs]=2
            res.append(crs)
            return True
        for c in range(numCourses):
            if state[c]==0:
                if not dfs(c):
                    return []
                    break
        return res

        