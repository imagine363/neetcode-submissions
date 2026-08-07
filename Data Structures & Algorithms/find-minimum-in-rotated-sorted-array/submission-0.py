class Solution:
    def findMin(self, nums):
        left = 0
        right = len(nums) -1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] > nums[right]:
                left = mid+1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                return nums[mid]
            
sol = Solution()
nums = [1,2,3,4,5,6]
print(sol.findMin(nums))

        