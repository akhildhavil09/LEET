class Solution(object):
    def maxAreaOfIsland(self, grid):
        def bfs(r,c):
            q= collections.deque()
            q.append((r,c))
            grid[r][c]=0
            area=1
            directions= [[1,0],[-1,0],[0,1],[0,-1]]
            while q:
                r1,c1= q.popleft()
                for dr,dc in directions:
                    nr,nc= r1+dr, c1+dc
                    if (nr) in range( rows) and (nc) in range (cols) and grid[nr][nc]==1:
                        q.append((nr,nc))
                        grid[nr][nc]=0
                        area+=1
            return area
        area=0
        rows,cols= len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    area= max(area,bfs(r,c))
        return area
            