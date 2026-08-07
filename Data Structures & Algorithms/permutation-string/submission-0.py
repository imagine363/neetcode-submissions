class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        s1dict = {}
        l = len(s1)
        for i in s1:
            if i not in s1dict:
                s1dict[i] = 1
            else:
                s1dict[i] += 1
        s2dict = {}
        for right in range(len(s2)):
            if s2[right] not in s2dict:
                s2dict[s2[right]] = 1
            else:
                s2dict[s2[right]] += 1
            while (right-left+1) > l:
                s2dict[s2[left]] -= 1
                if s2dict[s2[left]] == 0:
                    s2dict.pop(s2[left],None)
                left += 1
            if s1dict == s2dict:
                return True
        return False


sol = Solution()
s1 = "abc"
s2 = "lecaabee"
print(sol.checkInclusion(s1,s2))