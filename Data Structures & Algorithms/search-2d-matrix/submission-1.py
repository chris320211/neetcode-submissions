class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # given m x n 2d array matrix, int target
        # each row is increasing order
        # first int of each row is greater than last of prev
        # return true if target is in matrix
        # return false otherwise
        # binary search where we can find middle, see if greater or less than
        # binary search by col first then row
        # [0 1 2 ]
        # [3 4 5]
        # [7 8 9]
        # matrix[i][0], left pointer is i = 0, right pointer is len(matrix)
        cols = len(matrix[0])
        rows = len(matrix)

        top = 0
        bot = rows - 1

        while top <= bot:
            mid = (top + bot) // 2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bot = mid - 1
            else:
                break
        
        row = (top + bot) // 2

        if top > bot:
            return False

        left = 0
        right = cols - 1
        
        while left <= right:
            mid = (left + right) // 2
            if target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                return True
        return False
                