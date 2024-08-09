from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        q = deque()
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        rows, cols = len(grid), len(grid[0])
        minutes = 0
        
        # Initialize the queue with all rotten oranges and count fresh oranges
        fresh_oranges = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1
        
        # BFS to rot adjacent oranges
        while q and fresh_oranges > 0:
            minutes += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        # Rot the fresh orange and add to the queue
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh_oranges -= 1
        
        # If there are still fresh oranges left, return -1
        return -1 if fresh_oranges > 0 else minutes
