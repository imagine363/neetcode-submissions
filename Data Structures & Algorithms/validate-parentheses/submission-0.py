
class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        for i in s:
            if  i == "(" or i == "[" or i == "{":
                stack.append(i)
            elif stack and i == ")" and stack[-1] == "(":
                stack.pop(-1)
            elif stack and i == "}" and stack[-1] == "{":
                stack.pop(-1)
            elif stack and i == "]" and stack[-1] == "[":
                stack.pop(-1)
            else:
                return False
        return len(stack) == 0
sol = Solution() 
s = "[(])"
print(sol.isValid(s))
