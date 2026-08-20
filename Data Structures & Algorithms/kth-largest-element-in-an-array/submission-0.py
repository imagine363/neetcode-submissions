import heapq
class Solution:
    def findKthLargest(self, nums, k):
        hnums = []
        heapq.heapify(hnums)

        for x in nums:
            heapq.heappush(hnums,x)
            if len(hnums) > k:
                heapq.heappop(hnums)
        return hnums[0]

nums = [2,3,1,1,5,5,4]
k = 3
sol = Solution()
print(sol.findKthLargest(nums,k))