class Solution(object):
    def numIslands(self, grid):
        visited=set()
        def bfs(r,c):
            q= collections.deque()
            q.append((r,c))
            visited.add((r,c))
            while q:
                row,col=q.popleft()
                directions= [[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    nr,nc= row+dr, col+dc
                    if (nr) in range(rows) and (nc) in range(cols) and grid[nr][nc]=="1" and (nr,nc) not in visited:
                        q.append((nr,nc))
                        visited.add((nr,nc))
        island=0
        rows,cols= len(grid), len(grid[0])
        for r in range (rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visited:
                    bfs(r,c)
                    island+=1
        return island
