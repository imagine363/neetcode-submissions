class Solution:
    def lengthOfLongestSubstring(self, s):
        left = 0
        best = 0
        seen = set()
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            best = max(best,len(seen))
        return best
sol = Solution()
s = "zxyzxyz"
print(sol.lengthOfLongestSubstring(s))
