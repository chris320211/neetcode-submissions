from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # bfs, dfs
        # nested for loop to iterate through grid
        # each one we call dfs
        # base case is 0, in visited set, out of bounds
        # return and keep calling dfs

        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        islands = 0

        def dfs(r, c):
            if r not in range(rows):
                return
            if c not in range(cols):
                return
            if grid[r][c] == '0':
                return
            if (r, c) in visited:
                return

            visited.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    dfs(r, c)
                    islands += 1
        return islands



