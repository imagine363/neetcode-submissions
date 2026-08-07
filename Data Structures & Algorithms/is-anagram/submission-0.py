class Solution:
    def isAnagram(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        count = {}
        for c in s1:
            count[c] = count.get(c,0) + 1
        for c in s2:
            if c not in count:
                return False
            count[c] -= 1
            if count[c] < 0:
                return False
        return True
s = "racecar"
t = "carrace"
sol = Solution()
print(sol.isAnagram(s,t))

