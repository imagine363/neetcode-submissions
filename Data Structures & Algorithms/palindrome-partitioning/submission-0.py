class Solution:
    def isPalindrome(self,s):
        return s == s[::-1]
    def partition(self, s):
        res = []
        comb = []
        def backtrack(start):
            if start == len(s):
                res.append(comb.copy())
                return
            for end in range(start,len(s)):
                if self.isPalindrome(s[start:end+1]):
                    comb.append(s[start:end+1])
                    backtrack(end+1)
                    comb.pop()
        backtrack(0)
        return res
                
sol = Solution()
s = "aab"
print(sol.partition(s))

                    
            
        