class Solution:
    
    def groupAnagrams(self, strs):
        group = {}
        for i in strs:
            key = "".join(sorted(i))
            if key not in group:
                group[key] = []
            group[key].append(i)
        return list(group.values())
        
        
sol  = Solution()
strs = ["act","pots","tops","cat","stop","hat"]
print(sol.groupAnagrams(strs))
        