class Solution:
    def letterCombinations(self, digits):
        phone = {"2": "abc","3": "def","4": "ghi","5": "jkl","6": "mno","7": "pqrs","8": "tuv","9": "wxyz"}

        res = []
        comb = []
        def backtrack(start):
            if len(comb) == len(digits):
                res.append("".join(comb))
                return
            for i in range(len(phone[digits[start]])):
                comb.append(phone[digits[start]][i])
                backtrack(start+1)
                comb.pop()
        if not digits:
            return []
        backtrack(0)
        return res

sol = Solution()
digits = "34"
print(sol.letterCombinations(digits))

        