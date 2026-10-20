class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we can sort
        # a-z at most 26 char
        # count array, count how many char in each string
        # key is count, value is list of strs that have that count
        # lists cannot be keyed so must be tuple
        dict = {}

        for s in strs:
            count = [0] * 26
            for i in range(len(s)):
                count[ord(s[i]) - ord('a')] += 1
            if tuple(count) not in dict:
                dict[tuple(count)] = []
            dict[tuple(count)].append(s)
        return list(dict.values())
