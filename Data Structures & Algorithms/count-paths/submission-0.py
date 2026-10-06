class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # m x n, always start top left
        # recursion from each square we have two choices
        # any spot in grid can reach the end
        # DFS, cache[r][c], store each position and number of ways we
        # reach the end
        # result = R + D
        # R = R + D
        # D = R + D
        # base case = from the end, which is 1 path since
        # left and up only has 1 way to get to end
        # everything in bottom row is 1, right edge is also 1

        # bottom row where all is 1
        row = [1] * n

        # go through each row above bottom row
        for i in range(m - 1):
            newRow = [1] * n
            # check all from 2nd to last position reversed
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]
