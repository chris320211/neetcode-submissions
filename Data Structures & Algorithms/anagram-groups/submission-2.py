class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # array of strings
        # group all anagrams into sublist return a list with this sublists
        # anagram is where all character are the same
        # one approach is to sort
        
        # dictionary, count approach3
        # dict = {} # dictionary to track the lettercount and strings
        # for str in strs:
        #     count = [0] * 26 # for 26 letters
        #     for char in str:
        #         count[ord(char) - ord('a')]+= 1
                
        #     key = tuple(count) #tuples are hashable
        #     if key not in dict:
        #         dict[key] = []
        #     dict[key].append(str)
        # return list(dict.values())

        # time complex O(m * n) if m is strs and n is chars, two loops
        # space complex O(m) if m is strs, elements in dict

        # sort method
        # sorted(str) -> a list like ['a', 'b'...]
        # ''.join(sorted(str)) recombines, if they are equal we add
        # again dict for the list and the sorted str
        dict = {}
        for str in strs:
            sorted_str = ''.join(sorted(str))
            if sorted_str not in dict:
                dict[sorted_str] = []
            dict[sorted_str].append(str)
        return list(dict.values())

        # O(m * n log n) time complex
        # O(m * n) space complexity
