class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # m x n grid, return int, possible unique paths to the end
        # from beginning
        # only allowed to move up or down
        # recursive 
        # entire bottom row is only 1 unique path for each square
        # same thing with right side
        # square paths = right square paths + bottom square paths
        # m = num of rows
        # n = num col

        row = [1] * n
        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j +1 ] + row[j]
            row = newRow
        return row[0]
