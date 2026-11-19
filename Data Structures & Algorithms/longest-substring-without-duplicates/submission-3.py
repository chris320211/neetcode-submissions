class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # given a string s
        # find the length of longest substring w/o duplicates
        # duplicates, hashSet
        # two pointer
        # "zxyyxyz"
        #  i  j
        # hashset = zxy
        # len of hashset for length

        charSet = set()
        res = 0
        l = 0

        for i in range(len(s)):
            while s[i] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[i])
            count = len(charSet)
            res = max(count, res)
        
        return res