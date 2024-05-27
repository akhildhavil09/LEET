class Solution(object):
    def numIslands(self, grid):
        if not grid: return 0
        rows,cols= len(grid),len(grid[0])
        visit=set()
        island=0
        def dfs(r,c):
            if (r not in range(rows) or c not in range(cols) or (r,c) in visit or grid[r][c]=="0"):
                return
            visit.add((r,c))
            directions=[[1,0],[-1,0],[0,1],[0,-1]]
            for dr,dc in directions:
                dfs(r+dr,c+dc)
        for r in range (rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visit:
                    dfs(r,c)
                    island+=1
        return island        