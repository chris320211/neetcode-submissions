class Solution:
    def isPalindrome(self, s: str) -> bool:
        # given a string s, return true palindrome, return false
        # "tab a cat"
        #  012345678
        # even and odd case
        i = 0
        j = len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
