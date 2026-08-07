class Solution:
    def hasDuplicate(self, nums):
        return len(set(nums)) != len(nums)
sol = Solution()
nums = [5, 4, 3, 2, 1]
print(sol.hasDuplicate(nums))