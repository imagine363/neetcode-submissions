class Solution:
    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort()
        def backtrack(start, currcomb, currsum):
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                currcomb.append(candidates[i])
                currsum += candidates[i]

                if currsum < target:
                    backtrack(i+1, currcomb, currsum)

                if currsum == target:
                    res.append(currcomb.copy())

                currcomb.pop()
                currsum -= candidates[i]
        backtrack(0,[],0)
        return res


sol = Solution()
candidates = [9,2,2,4,6,1,5]
target = 8
print(sol.combinationSum2(candidates,target))
        