class Solution:
    def threeSum(self, nums):
        res = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i+1
            right = len(nums) - 1

            while left < right:
                currsum = nums[i] + nums[left] + nums[right]
                if currsum > 0:
                    right -= 1
                elif currsum < 0:
                    left += 1
                elif currsum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left +=1
                    right -= 1
                    while left < right and nums[left-1] == nums[left]:
                        left += 1
                    while left < right and nums[right+1] == nums[right]  :
                        right-=1
        return res

sol = Solution()
nums = [0,1,1]
print(sol.threeSum(nums))
