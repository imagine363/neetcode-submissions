import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks, n):
        freq = {}
        for task in tasks: 
            if task in freq:
                freq[task] += 1
            else:
                freq[task] = 1

        freqval = freq.values()
        freqval = [-x for x in freqval]
        heapq.heapify(freqval)

        time = 0
        tempq = deque()
        while tempq or freqval:
            while tempq and time >= tempq[0][0]:
                heapq.heappush(freqval,-tempq.popleft()[1])

            if not freqval and tempq:
                time = tempq[0][0]
                continue
            x = -heapq.heappop(freqval)
            x -= 1  

            if x > 0:
                tempq.append((time+ n+1, x))

            time += 1
        return time
    
tasks = ["A","A","A","B","B","B"]
n = 2
sol = Solution()
print(sol.leastInterval(tasks,n))
            



        


