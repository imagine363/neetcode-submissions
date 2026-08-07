class Solution:
    def isValidSudoku(self, board):
        for i in range(9):
            seen = set()
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                if val not in "123456789":
                    return False
                if val in seen:
                    return False
                seen.add(val)
        for i in range(9):
            seen = set()
            for j in range(9):
                val = board[j][i]
                if val == ".":
                    continue
                if val in seen:
                    return False
                seen.add(val)
        for r in range(0,9,3):
            for c in range(0,9,3):
                seen = set()
                for i in range(r,r+3):
                    for j in range(c,c+3):
                        val = board[i][j]
                        if val == ".":
                            continue
                        if val in seen:
                            return False
                        seen.add(val)
        return True
board = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

sol = Solution()
print(sol.isValidSudoku(board))