class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # array of strings
        # group all anagrams into sublist return a list with this sublists
        # anagrams are all same character
        # sort
        # anagram if sorted is same
        # hashmap key = sorted str, value = [str]

        dict = {}

        for str in strs:
            sorted_str = ''.join(sorted(str)) # sort(str), str ='cba', give us 'a', 'b', 'c' as list
            if sorted_str not in dict:
                dict[sorted_str] = []
            dict[sorted_str].append(str)
        return list(dict.values())

        #