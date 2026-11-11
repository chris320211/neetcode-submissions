class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 2d array grid, 1 represent land, 0 represemt water
        # count and return number of islands
        # bfs approach
        if len(grid) == 0:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])

        visit = set()
        islands = 0

        def bfs (r, c):
            # bfs is iterative, using queue for memory
            q = collections.deque() #last in first out
            visit.add((r, c)) # add as visited
            q.append((r, c))# add to our queue

            while len(q) != 0:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if (r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        return islands
