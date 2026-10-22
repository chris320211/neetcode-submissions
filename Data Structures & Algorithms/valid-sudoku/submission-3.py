class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 2d array
        # each row no dupl
        # each col no dupl
        # each sub square no dupl
        # hashsets, hashmap
        # subsquares, r // 3, c //3, key by a pair (r // 3, c // 3)

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in rows[r]:
                    return False
                rows[r].add(board[r][c])
                if board[r][c] in cols[c]:
                    return False
                cols[c].add(board[r][c])
                if board[r][c] in squares[(r // 3, c // 3)]:
                    return False
                squares[(r // 3, c // 3)].add(board[r][c])
        
        return True
                    