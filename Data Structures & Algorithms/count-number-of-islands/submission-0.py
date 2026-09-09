from collections import deque
class Solution:
    def numIslands(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        land = set()
        count  = 0

        def bfs(row,col):
            directions = [(0,-1),(-1,0),(0,1),(1,0)]
            q = deque()
            q.append((row,col))
            land.add((row,col))
            while q:
                row,col = q.popleft()
                for r,c in directions:
                    newrow = row+r
                    newcol = col+c
                    if 0 <= newrow < rows and 0 <= newcol < cols and grid[newrow][newcol] == '1' and (newrow,newcol) not in land:
                        q.append((newrow,newcol))
                        land.add((newrow,newcol))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in land:
                    bfs(r,c)
                    count += 1
        return count


grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]
sol = Solution()
print(sol.numIslands(grid))