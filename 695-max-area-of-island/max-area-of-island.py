class Solution(object):
    def maxAreaOfIsland(self, grid):
        area = 0
        
        def dfs(r, c):
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 1:
                grid[r][c] = 0  # Mark the cell as visited
                return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)
            return 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    area = max(area, dfs(r, c))
        
        return area
