class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        prehash={i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prehash[crs].append(pre)
        
        visit=set()
        def dfs(crs):
            if crs in visit:return False
            if prehash[crs]==[]: return True
            visit.add(crs)
            for pre in prehash[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            prehash[crs]=[]
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
    
        