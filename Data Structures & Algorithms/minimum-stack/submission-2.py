class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
    def push(self, val: int) -> None:
        # adds to stack
        self.stack.append(val)
        if len(self.minStack) != 0:
            val = min(val, self.minStack[-1])
            self.minStack.append(val)
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        # removes from stack
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        # returns top element
        return self.stack[-1]

    def getMin(self) -> int:
        # get min
        return self.minStack[-1]
        
