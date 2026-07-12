class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # two string s and t
        # return true is anagram
        # anagram = string same characters, order diff
        # else return false

        if len(s) != len(t):
            return False

        # keep track of seen characters via hashamp, two
        s_map = {}
        t_map = {}

        for char in s:
            if char not in s_map:
                s_map[char] = 0
            s_map[char] += 1

        for char in t:
            if char not in t_map:
                t_map[char] = 0
            t_map[char] += 1

        if s_map == t_map:
            return True
        return False
