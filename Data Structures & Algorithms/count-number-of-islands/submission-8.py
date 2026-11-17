from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
       # 2d grid, string 1 represents land
       # string 0 is water
       # return num of islands
       # connected 1s horizontla or verticlaly, surrounded by water, edge is water

       # bfs
       # call bfs on newly discovered 1s, to discover the whole island
       # visited set of 1s
       # bfs we need a queue, frontier
       # we add to frontier, from that unit, we check in 4 directions if 1
       # we add cordinate to queue
       # while queue, keep checking

        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        islands = 0

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))

            directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    newR = r + dr
                    newC = c + dc
                    if newR in range(rows) and newC in range(cols) and (newR, newC) not in visited and grid[newR][newC] == '1':
                        q.append((newR, newC))
                        visited.add((newR, newC))
                

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == '1':
                    bfs(r, c)
                    islands += 1
        
        return islands


