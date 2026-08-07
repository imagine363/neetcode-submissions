from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        window = deque()
        res = []
        left = 0
        for right in range(len(nums)):
            while window and nums[right] > nums[window[-1]]:
                window.pop()
            window.append(right)
            if (right - left+1) == k:
                res.append(nums[window[0]])
                if window[0] == left:
                    window.popleft()
                left+= 1
        return res

sol = Solution()
nums = [4, 2, 12, 3, 8, 7]
k = 3
print(sol.maxSlidingWindow(nums,k))