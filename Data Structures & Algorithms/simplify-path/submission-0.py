class Solution:
    def simplifyPath(self, path: str) -> str:
        # absolute path for unix file system path
        # always begins with /
        # transofrm it into simplified canonical
        # . is curr dir
        # .. is prev
        # multiple consecutive / can be treated as single /
        # epriods more than 2 are valid names 
        # 
        # read input from left to right
        # "/neetcode/practice//...///../courses"
        # go into neetcode direc
        # go into practice dir
        # /neetcode/practice/courses
        # we ignore /...///.. since ignore consectuive / and ... is a directory
        # /// consectuvie is ignored, 
        # /neetcode/practice/.../..
        # if we see /.. we pop from top of stack, if see one dot we ignore
        # if we see consectuvie / we ignore
        path += '/'
        stack = []
        cur = ''

        for i in range(len(path)):
            if path[i] == '/': # if a new directory
                if cur == '..': # if what we build is .., we pop
                    if stack: 
                        stack.pop()
                elif cur != '' and cur != '.': # if not empty so non / and not . we add
                    stack.append(cur)
                cur = '' # after we see a new direc, we reset cur
            else:
                cur += path[i] # build file name
        
        res = ''
        for item in stack:
            res += '/'
            res += item
        
        if res == '':
            return '/'
        return res
        