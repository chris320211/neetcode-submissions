class Solution:
    def isValid(self, s: str) -> bool:
        # given a string s of (), {}, []
        # determine if it is valid via open and closed
        # using a stack, i add then i take out from back

        stack = []
        # example ([])
        # stack [ open ]
        for i in range(len(s)):
            # check if open, add to stack
            if s[i] == "[" or s[i] == "(" or s[i] == "{":
                stack.append(s[i])
            # check if closing, if it is we check if open in stck
            if s[i] == "]":
                if len(stack) == 0 or stack.pop() != "[":
                        return False
            if s[i] == "}":
                if len(stack) == 0 or stack.pop() != "{":
                        return False
            if s[i] == ")":
                if len(stack) == 0 or stack.pop() != "(":
                        return False
        return len(stack) == 0
            
            

