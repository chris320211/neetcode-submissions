class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # input two string s and t
        # return true if valid anagram
        # if same characters return true
        # hashmap build or sort
        
        if len(s) != len(t):
            return False
        
        dict_s = {}
        dict_t = {}
        for i in range(len(s)):
            if s[i] not in dict_s:
                dict_s[s[i]] = 0
            dict_s[s[i]] += 1
            if t[i] not in dict_t:
                dict_t[t[i]] = 0
            dict_t[t[i]] += 1
        
        if dict_s == dict_t:
            return True
        else:
            return False