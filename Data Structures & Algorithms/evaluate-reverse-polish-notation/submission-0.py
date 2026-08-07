class Solution:
    def evalRPN(self, tokens):
        stack = list()
        for i in tokens:
            if i not in {"+","-","*","/"}:
                stack.append(int(i))
            elif i == "+":
                a = stack.pop()
                b = stack.pop()
                c =  a+b
                stack.append(c)
            elif i == "-":
                b = stack.pop()
                a = stack.pop()
                c =  a-b
                stack.append(c)
            elif i == "*":
                a = stack.pop()
                b = stack.pop()
                c =  a*b
                stack.append(c)
            elif i == "/":
                b = stack.pop()
                a = stack.pop()
                c =  int(a/b)
                stack.append(c)
        return stack[0]

sol = Solution()
tokens = ["1","2","+","3","*","4","-"]
print(sol.evalRPN(tokens))
