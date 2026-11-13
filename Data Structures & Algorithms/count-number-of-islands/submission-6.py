from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # given a 2D array grid '1' is alnd, 0 is water
        # return num of islands
        # bfs on when we find 1, to discover entire island
        # keep set to ensure we dont see already seen elements
        # bfs queue to discover, frontier

        # nested for loop 

        rows = len(grid)
        cols = len(grid[0])

        islands = 0
        visited = set()

        def bfs(r, c):
            q = deque()
            visited.add((r, c))
            q.append((r,c))
            while q:
                row, col = q.popleft()
                directions = [[1,0], [0,1],[-1,0],[0,-1]]
                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc
                    if new_row in range(rows) and new_col in range(cols) and (new_row, new_col) not in visited and grid[new_row][new_col] == '1':
                        visited.add((new_row, new_col))
                        q.append((new_row, new_col))




        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == '1':
                    bfs(r, c)
                    islands += 1
        return islands



