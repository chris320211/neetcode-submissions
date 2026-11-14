# stack class, 4 methods
# push, pop, top, get min
# O(1)
# stack -> python array
# minStack -> python array
# push operation
# add to the stack, append
# O(1)
# check if new element is less than minStack top
# if less than we add to minStack.append
# if not we add the top again via append
# pop operation
# stack.pop, o(1)
# pop both from stack and minStack
# return stack
# top operation
# stack[-1] returns top
# o(1)
# getMin
# stack = [1, 0, 2, 4
# stack(min) = [1, 0, 0, 0
# return minStack[-1]

class MinStack:
    
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        self.stack.append(val)
        if len(self.minStack) == 0:
            self.minStack.append(val)
        else:
            prevMin = self.minStack[-1]
            self.minStack.append(min(val, prevMin))

    def pop(self):
        self.stack.pop()
        self.minStack.pop()
    
    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minStack[-1]
