class Solution:
    def largestRectangleArea(self, heights):
        stack = list()
        maxsize = 0
        for i in range(len(heights)+1):
            start = i
            if i == len(heights):
                curr_height = 0
            else:
                curr_height = heights[i]
            while stack and curr_height < stack[-1][1]:
                indx = stack.pop()

                start = indx[0]
                height = indx[1]

                width  = i - start
                maxsize = max(maxsize,height*width)
            if i != (len(heights)):
                stack.append((start,curr_height))
        return maxsize
sol = Solution()
heights = [1,3,7]
print(sol.largestRectangleArea(heights))