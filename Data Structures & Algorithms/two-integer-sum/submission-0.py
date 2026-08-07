class Solution:
    def twoSum(self,nums,target):
        seen = {}
        for i, num in enumerate(nums):
            c = target - num
            if c in seen:
                return [seen[c], i]
            seen[num] = i
nums = [3,4,5,6]
target = 7
sol = Solution()
print(sol.twoSum(nums,target))