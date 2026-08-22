class Solution:
    def subsets(self, nums):
        res = []
        path = []
        start = 0
        def backtrack(start):
            res.append(path.copy())
            for i in range(start,len(nums)):
                path.append(nums[i])
                backtrack(i+1)
                path.pop()
        backtrack(0)
        return res
sol = Solution()
nums = [1,2,3]
print(sol.subsets(nums))
