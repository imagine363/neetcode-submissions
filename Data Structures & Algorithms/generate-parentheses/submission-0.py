class Solution:
    def generateParenthesis(self, n):
        res = []
        path = []
        def backtrack(open, close):
            if open == close == n:
                res.append("".join(path))
                return
            if open < n:
                path.append("(")
                backtrack(open+1,close)
                path.pop()
            if close < open:
                path.append(")")
                backtrack(open,close+1)
                path.pop()
        backtrack(0,0)
        return res

sol = Solution()
n = 3
print(sol.generateParenthesis(n))
            


        