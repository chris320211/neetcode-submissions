from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # dfs approach
        # if we see 1 not in visied
        # call dfs, we want to return area
        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        result = 0

        def dfs(r, c):
            # base case
            if r not in range(rows) or c not in range(cols) or grid[r][c] == 0 or (r, c) in visited:
                return 0
            visited.add((r, c))
            return (1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1))
        
        for r in range(rows):
            for c in range(cols):
                result = max(result, dfs(r, c))
        return result