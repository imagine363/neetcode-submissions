import heapq
class KthLargest:

    def __init__(self, k, nums = None):
        self.k = k
        self.nums = nums if nums is not None else []

    def add(self, val):
        heapq.heapify(self.nums)
        heapq.heappush(self.nums,val)

        if len(self.nums) > self.k:
            for _ in range(len(self.nums)-self.k):
                heapq.heappop(self.nums)
                
        return self.nums[0]

