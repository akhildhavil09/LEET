class Solution(object):
    def orangesRotting(self, grid):
        rows,cols= len(grid), len(grid[0])
        q=deque()
        time,fresh=0,0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    q.append((r,c))
        def rotten(r,c):
            if (0<=r<rows and 0<=c<cols and grid[r][c]==1):
                grid[r][c]=2
                q.append((r,c))
                return 1
            return 0
        while q and fresh>0:
            for _ in range(len(q)):
                ro,co= q.popleft()
                fresh -= rotten(ro+1,co)
                fresh -= rotten(ro-1,co)
                fresh -= rotten(ro,co+1)
                fresh -= rotten(ro,co-1)
            time+=1
        return time if fresh==0 else -1
                        