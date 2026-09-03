class Solution:
    def solveNQueens(self, n):
        col = set()
        posDiag = set() # (r+c) up
        negDiag = set() # (r-c) down
        board  = [["."]*n for i in range(n)]
        res = []

        def backtrack(row):
            if row == n:
                res.append(["".join(r) for r in board])
                return
            for c in range(n):
                if c not in col and row+c not in posDiag and row-c not in negDiag:
                    board[row][c] = 'Q'
                    col.add(c)
                    posDiag.add(row+c)
                    negDiag.add(row-c)

                    backtrack(row+1)

                    board[row][c] = '.'
                    col.remove(c)
                    posDiag.remove(row+c)
                    negDiag.remove(row-c)
        backtrack(0)
        return res

n = 4
sol = Solution()
print(sol.solveNQueens(4))

                
