class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # array of strings
        # group all anagrams into sublist return a list with this sublists
        # anagram is where all character are the same
        # one approach is to sort
        
        # dictionary, count approach3
        dict = {} # dictionary to track the lettercount and strings
        for str in strs:
            count = [0] * 26 # for 26 letters
            for char in str:
                count[ord(char) - ord('a')]+= 1
                
            key = tuple(count) #tuples are hashable
            if key not in dict:
                dict[key] = []
            dict[key].append(str)
        return list(dict.values())