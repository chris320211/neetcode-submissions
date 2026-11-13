from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #bfs, dfs
        #bfs
        #nested for loop
        #find rotten fruit that we havent checked
        #bfs, queue, if adjacant fresh fruit, it is now rotten and we add them to queue
        #for each level, each time that happens we add 1 min
        #bfs returns the mins needed
        # iterate through the entire grid
        # find all rotten fruits add to queue
        # bfs queue, keep track of levels
        # we find first level fruits, add to queue
        # then go through it
        # that is one minute, then next level
        # len queue

        rows = len(grid)
        cols = len(grid[0])

        minutes = 0
        q = deque()

        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        
        size = len(q)
        while q:
            if size > 0:
                row, col = q.popleft()
                directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
                for dr, dc in directions:
                    newRow = row + dr
                    newCol = col + dc
                    if newRow in range(rows) and newCol in range(cols) and grid[newRow][newCol] == 1:
                        grid[newRow][newCol] = 2
                        fresh -= 1
                        q.append((newRow, newCol))
                size -= 1
            elif size == 0:
                minutes += 1
                size = len(q)
        
        if fresh == 0:
            return minutes
        else:
            return -1




                

        