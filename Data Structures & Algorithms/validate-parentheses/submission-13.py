class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c in map:
                if len(stack) != 0 and stack[-1] == map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if len(stack) == 0:
            return True
        else:
            return False
                

