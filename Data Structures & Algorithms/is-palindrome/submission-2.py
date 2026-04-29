class Solution:
    def isPalindrome(self, s: str) -> bool:
        # "tab a cat"
        # only alphanumeric .isalnum()
        
        # "tab a cat"
        # order from the front = order from the back
        # two pointer i and j
        # 0 index of string and s.length() - 1 of string
        # tab a c????at"
        # stopping point odd string i = j
        
        # 0 1 2 3 i > j 
        #   i j
        # 0 1 2 3 4
        #    j  i
            
        i = 0
        j = len(s) - 1

        while i < j:

            while i < j and s[i].isalnum() is False:
                i = i + 1
            while i < j and s[j].isalnum() is False:
                j = j - 1
            # .lower()

            if s[i].lower() != s[j].lower():
                return False
            i = i + 1
            j = j - 1
        
        return True


    