class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # given an array of strings strs, group all anagrams together
        # return the output in any order
        # key array from of length 26 to represent how many char

        strings = {}
        
        for s in strs:
            char = [0] * 26
            for c in s:
                char[ord(c) - ord('a')] += 1
            if tuple(char) not in strings:
                strings[tuple(char)] = []
            strings[tuple(char)].append(s)
        return list(strings.values())
