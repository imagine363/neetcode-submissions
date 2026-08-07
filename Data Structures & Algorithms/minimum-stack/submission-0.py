class MinStack:
    def __init__(self):
        self.stack = list()
        self.minstack = list()
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack:
            self.minstack.append(val)
        else:
            mini = min(val,self.minstack[-1])
            self.minstack.append(mini)
    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        if self.stack:
            top = self.stack[-1]
            return top

    def getMin(self) -> int:
        return self.minstack[-1]
stack = MinStack()

stack.push(-2)
stack.push(0)
stack.push(-3)

print(stack.getMin())   

stack.pop()

print(stack.top())    
print(stack.getMin())  

