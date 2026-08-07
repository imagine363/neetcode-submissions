class Solution:
    def characterReplacement(self, s , k):
        left = 0
        charcount = {}
        best = 0
        for right in range(len(s)):
            if s[right] not in charcount:
                charcount[s[right]] = 1
            else:
                charcount[s[right]] += 1 
            mostfreq = max(charcount.values())
            while (right-left+1) - mostfreq > k:
                charcount[s[left]] -= 1
                left += 1
            best = max(best,(right-left+1))
        return best
sol = Solution()
s = "AAABABB" 
k = 1
print(sol.characterReplacement(s,k))
