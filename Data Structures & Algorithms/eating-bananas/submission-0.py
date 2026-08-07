import math
class Solution:
    def minEatingSpeed(self, piles, h):
        left = 1
        right = max(piles)
        k=float('inf')
        while left <= right:
            mid = (left+right)//2
            total_h = 0
            for i in piles:
                total_h += math.ceil(i/mid)
            if total_h > h:
                left = mid+1
            elif total_h <= h:
                k = mid
                right = mid -1
        return k

sol = Solution()
piles = [1,4,3,2]
h = 9
print(sol.minEatingSpeed(piles,h))
        