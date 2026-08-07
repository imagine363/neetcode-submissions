class Solution:
    def findDuplicate(self, nums):
        s = nums[0]
        f = nums[0]
        while True:
            s = nums[s]
            f = nums[nums[f]]
            if s == f:
                break
        finder = nums[0]
        while finder != s:
            finder = nums[finder]
            s = nums[s]
        return finder
sol = Solution()
nums = [1,2,3,2,2]
print(sol.findDuplicate(nums))