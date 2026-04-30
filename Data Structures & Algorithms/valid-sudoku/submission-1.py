class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # each row must contan digits 1-9
        # each column mus tocntain digits 1-9
        # each nine 3x3 subbox must contain 1-9

        # hashmap
        # key: 9 rows, 9 colmns, 9 boxes
        # value: list[1-9]
        # for loop iterate through rows
        # for loop iterate through col
        # for loop iterate through 9 boxes
        #   0 1 2 3 4 5 6 7 8
        # 0
        # 1
        # 2
        # 3
        # 4
        # 5
        # 6
        # 7
        # 8

        rows = len(board)
        cols = len(board[0])

        dict = {}

        # iterate through rows
        for i in range(rows):
            row = i
            dict[row] = []
            for j in range(cols):
                if board[i][j] == '.' or board[i][j] == ',':
                    continue
                elif board[i][j] not in dict[row]:
                    dict[row].append(board[i][j])
                else:
                    return False 
    
        for i in range(cols):
            col = 9 + i
            dict[col] = []
            for j in range(rows):
                if board[j][i] == '.' or board[j][i] == ',':
                    continue
                elif board[j][i] not in dict[col]:
                    dict[col].append(board[j][i])
                else:
                    return False
        
        for br in range(3):
            for bc in range(3):
                key = 18 + br + bc
                dict[key] = []
                for row in range(br * 3, br * 3 + 3):
                    for col in range(bc * 3, bc * 3 + 3):
                        if board[row][col] == '.' or board[row][col] == ',':
                            continue
                        elif board[row][col] not in dict[key]:
                            dict[key].append(board[row][col])
                        else:
                            return False
        return True

        
                
