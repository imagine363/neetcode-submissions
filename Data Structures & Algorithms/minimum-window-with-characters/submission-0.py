class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        have = 0
        res = ""
        bestlen = float("inf")
        need = {}
        for i in t:
            if i not in need:
                need[i] = 1
            else:
                need[i] += 1
        window = {}
        for right in range(len(s)):
            if s[right] not in window:
                window[s[right]] = 1
            else:
                window[s[right]] += 1
            if s[right] in need and window[s[right]] == need[s[right]]:
                have += 1
            while have == len(need):
                if (right-left+1) < bestlen:
                    bestlen = right-left+1
                    res = s[left:right+1]
                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                if window[s[left]] == 0:
                    window.pop(s[left])
                left += 1
        return res
sol = Solution()
s = "xyz" 
t = "xyz"
print(sol.minWindow(s,t))