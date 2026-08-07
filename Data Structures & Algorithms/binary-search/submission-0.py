class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = int((left+right)/2)
            if nums[mid] < target:
                left = mid+1
            elif nums[mid] > target:
                right = mid-1
            elif nums[mid] == target:
                return mid
        return -1
sol = Solution()
nums = [-1,0,2,4,6,8]
target = 3
print(sol.search(nums,target))


        