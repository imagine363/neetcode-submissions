class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > nums[right]:
                if target > nums[right]:
                    if target > nums[mid]:
                        left = mid+1
                    else:
                        right = mid-1
                else:
                    left = mid+1
            else:
                if target <= nums[right]:
                    if target > nums[mid]:
                        left = mid+1
                    else:
                        right = mid-1
                else:
                    right = mid -1
        return -1

nums = [3,4,5,6,1,2]
target = 2
sol = Solution()
print(sol.search(nums,target))