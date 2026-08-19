import math
import heapq
class Solution:
    def kClosest(self, points, k):
        dis = []
        heapq.heapify(dis)
        for x in points:
            x1 = x[0]
            x2 = x[1]
            heapq.heappush(dis,[-(math.sqrt((x1)**2 + (x2)**2)),x1,x2])
            if len(dis) > k:
                heapq.heappop(dis)  
        res = []
        for element in dis:
            res.append([element[1],element[2]])

        
        return res
            
points = [[0,2],[2,2]]
k = 1
sol = Solution()
print(sol.kClosest(points,k))