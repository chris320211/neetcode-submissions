class Solution:
    def isValid(self, s: str) -> bool:
        # string s consists of parentheses, open or closing
        # stack, add all the open paratheses to stack
        # pop stack check if first closing paraetheses matches
        # loop through s
        # check if its open, if it is we add to stack
        # if it is closed, we pop from stack and we check if they match

        stack = []
        
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '['  or s[i] == '{':
                stack.append(s[i])
            if s[i] == ')':
                if not stack:
                    return False
                open = stack.pop()
                if open != '(':
                    return False
            if s[i] == ']':
                if not stack:
                    return False
                open = stack.pop()
                if open != '[':
                    return False
            if s[i] == '}':
                if not stack:
                    return False
                open = stack.pop()
                if open != '{':
                    return False
        if not stack:
            return True
        else:
            return False
                

