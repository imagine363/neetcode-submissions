class Solution:
    def permute(self, nums):
        res = []
        seen = [False] * len(nums)
        def backtrack(currcomb):
            if len(currcomb) == len(nums):
                res.append(currcomb.copy())
            for i in range(len(nums)):
                if seen[i]:
                    continue
                    
                seen[i] = True
                currcomb.append(nums[i])

                backtrack(currcomb)

                currcomb.pop()
                seen[i] = False
        backtrack([])
        return res
                
sol = Solution()
nums = [1,2,3]
print(sol.permute(nums))
        