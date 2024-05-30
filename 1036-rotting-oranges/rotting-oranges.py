from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh, time = 0, 0
        
        # Initialize the queue with all rotten oranges and count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        
        def convert(r, c):
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                grid[r][c] = 2
                q.append((r, c))
                return 1
            return 0
        
        # BFS process
        while q and fresh > 0:
            # Process all oranges in the current level of BFS
            for _ in range(len(q)):
                row, col = q.popleft()
                fresh -= convert(row + 1, col)
                fresh -= convert(row - 1, col)
                fresh -= convert(row, col + 1)
                fresh -= convert(row, col - 1)
            time += 1
        
        return time if fresh == 0 else -1
