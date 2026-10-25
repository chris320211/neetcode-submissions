class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # given an array of strs, group all anagrams into sublists
        # hashmap key by a tuple, array to tuple
        # key is 26 index array of 0
        # value is going to be a list: strings
        # return list(hashmap.values()
        # the char ord - ord a

        dict = {}

        for s in strs:
            count = [0] * 26
            for char in s:
                index = ord(char) - ord('a')
                count[index] += 1
            tupCount = tuple(count)
            if tupCount not in dict:
                dict[tupCount] = []
            dict[tupCount].append(s)
        return list(dict.values())


