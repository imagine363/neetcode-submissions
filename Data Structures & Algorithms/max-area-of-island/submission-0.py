from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        land = set()
        maxsize = 0
        def bfs(row,col):
            directions = [(0,-1),(-1,0),(0,1),(1,0)]
            q = deque()
            q.append((row,col))
            land.add((row,col))
            size = 1
            while q:
                row,col = q.popleft()
                for r,c in directions:
                    newrow = row+r
                    newcol = col+c
                    if 0 <= newrow < rows and 0 <= newcol < cols and grid[newrow][newcol] == 1 and (newrow,newcol) not in land:
                        size += 1
                        q.append((newrow,newcol))
                        land.add((newrow,newcol))
            nonlocal maxsize
            if size > maxsize:
                maxsize = size
                        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in land:
                    bfs(r,c)
        return maxsize


grid = [
  [0,1,1,0,1],
  [1,0,1,0,1],
  [0,1,1,0,1],
  [0,1,0,0,1]
]
sol = Solution()
print(sol.maxAreaOfIsland(grid))
        