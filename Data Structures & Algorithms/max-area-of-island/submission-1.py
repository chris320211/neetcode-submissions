from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # bfs, dfs
        # nested for loop, iterate throuhg each spot
        # bfs function
        # visited set
        # bfs
        # queue (frontier), for directions

        rows = len(grid)
        cols = len(grid[0])

        result = 0
        visited = set() # (r, c)

        def bfs(r, c):
            q = deque()
            visited.add((r, c))
            q.append((r, c))
            area = 1
            while q:
                row, col = q.popleft()
                directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
                for dr, dc in directions:
                    newRow = row + dr
                    newCol = col + dc
                    if (newRow, newCol) not in visited and newRow in range(rows) and newCol in range(cols) and grid[newRow][newCol] == 1:
                        area += 1
                        visited.add((newRow, newCol))
                        q.append((newRow, newCol))
            return area

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == 1:
                    returned = bfs(r, c)
                    result = max(result, returned)
        return result