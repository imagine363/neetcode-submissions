class Solution:
    def dailyTemperatures(self, temperatures):
        stack = list()
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                indx = stack.pop()
                res[indx] = i - indx
            stack.append(i)
        return res
sol = Solution()
temperatures = [30,38,30,36,35,40,28]
print(sol.dailyTemperatures(temperatures))