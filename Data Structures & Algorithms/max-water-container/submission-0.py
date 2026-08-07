class Solution:
    def maxArea(self, heights):
        left = 0
        right = len(heights)-1
        res = 0
        while left < right:
            area = (right-left) * min(heights[left],heights[right])
            res = max(res,area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return res
sol = Solution()
height = [1,7,2,5,4,7,3,6]
print(sol.maxArea(height))
        