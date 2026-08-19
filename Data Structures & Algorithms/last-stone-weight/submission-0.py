import heapq
class Solution:
    def lastStoneWeight(self, stones):
        maxheap = [-x for x in stones]
        heapq.heapify(maxheap)
        heapstones = maxheap
        while len(heapstones) > 1:
            x = -heapq.heappop(heapstones)
            y = -heapq.heappop(heapstones)

            if x == y:
                continue
            elif x > y:
                heapq.heappush(heapstones, -(x-y))
            elif x < y:
                heapq.heappush(heapstones, -(y-x))
        return -heapstones[0] if heapstones else 0

stones = [2,3,6,2,4]
