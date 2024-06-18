class Solution(object):
    def numIslands(self, grid):
        directions=[[1,0],[0,1],[0,-1],[-1,0]]
        rows,cols=len(grid),len(grid[0])
        def dfs(r,c):
            grid[r][c]="0"
            for dr,dc in directions:
                nr,nc= r+dr, c+dc
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]=="1":
                    dfs(nr,nc)
        count=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1":
                    count+=1
                    dfs(r,c)

        return count        