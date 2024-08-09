class Solution(object):
    def orangesRotting(self, grid):
        q=deque()
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        time,fresh=0,0
        rows,cols=len(grid),len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    q.append((r,c))
                elif grid[r][c]==1:
                    fresh+=1
        
        while q and fresh>0:
            time+=1
            for _ in range(len(q)):
                r,c=q.popleft()
                for dr,dc in directions:
                    nr,nc= r+dr, c+dc
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        q.append((nr,nc))
                        fresh-=1
        return -1 if fresh>0 else time
