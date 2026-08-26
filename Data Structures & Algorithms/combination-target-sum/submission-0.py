class Solution:
    def combinationSum(self, nums, target):
        res = []
        def backtrack(start, currcomb, currsum):
            for i in range(start, len(nums)):
                currcomb.append(nums[i])
                currsum += nums[i]

                if currsum < target:
                    backtrack(i, currcomb, currsum)

                elif currsum == target:
                    res.append(currcomb.copy())

                currcomb.pop()
                currsum -= nums[i]
        backtrack(0,[],0)
        return res
            



sol = Solution()
nums = [2,5,6,9]
target = 9
print(sol.combinationSum(nums,target))