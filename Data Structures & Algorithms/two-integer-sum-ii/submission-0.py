class Solution:
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers)-1
        while left<right:
            currsum = numbers[left] + numbers[right]
            if currsum > target:
                right -= 1
                currsum = numbers[left] + numbers[right]
            elif currsum < target:
                left += 1
                currsum = numbers[left] + numbers[right]
            elif currsum == target:
                return [left+1,right+1]
sol = Solution()
numbers = [1,2,3,4] 
target = 3
print(sol.twoSum(numbers,target))
