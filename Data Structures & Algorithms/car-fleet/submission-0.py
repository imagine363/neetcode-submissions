class Solution:
    def carFleet(self, target, position, speed):
        stack = list()
        cars = list(zip(position,speed))
        cars.sort(reverse=True)
        for pos,spd in cars:
            time = (target-pos)/spd
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
sol = Solution()
target = 10
position = [1,4]
speed = [3,2]
print(sol.carFleet(target,position,speed))