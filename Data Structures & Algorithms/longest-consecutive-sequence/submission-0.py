class Solution:
    def longestConsecutive(self, nums):
        seen = set(nums)
        r = 0
        for i in nums:
            if i-1 not in seen:
                count = 1
                while i+1 in seen:
                    count += 1
                    i+=1
                if count > r:
                    r = count
        return r
sol = Solution()
nums = [2,20,4,10,3,4,5]
print(sol.longestConsecutive(nums))
        