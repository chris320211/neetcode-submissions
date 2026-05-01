
# design a stack class supports 4 oeprations
# all should run in O(1)
# stack adds to top (end of array), removes from top (end of array)
# push is add to top so O(1)
# pop is remove from top so O(1)
# top is get the top O(1)
# getMin, normally take O(N), array we need to scan through entire and compare
# 
# secondary stack keep track of the minimum at that level of orignal stack
# stack [1 2 ]
# minStack [1 1 ]

# push and pop oepration on minstack


class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack == []:
            self.minStack.append(val)
        elif self.minStack[-1] > val:
            self.minStack.append(val)
        elif self.minStack[-1] <= val:
            self.minStack.append(self.minStack[-1])

    def pop(self) -> None:
        del self.stack[-1]
        del self.minStack[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

    # stack[-1, 1,]
    # minStack [-1 -1,]
        
