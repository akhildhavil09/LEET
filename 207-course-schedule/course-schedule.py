class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph={i:[] for i in range(numCourses)}


        for crs1,crs2 in prerequisites:
            graph[crs1].append(crs2)

        visiting,visited=set(), set()

        def hasCycle(crs):
            if crs in visiting:
                return True # has cycle
            if crs in visited:
                return False # no cycle found for this crs

            visiting.add(crs)
            for nei in graph[crs]:
                if hasCycle(nei):
                    return True
            visiting.remove(crs)
            visited.add(crs)
            return False
        for crs in range(numCourses):
            if hasCycle(crs):
                return False
        return True
