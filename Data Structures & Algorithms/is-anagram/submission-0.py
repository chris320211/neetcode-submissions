class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hashmap so dict, key and value, we store the letter as key and index as value
        
        # given two strings and t, if anagram -> true, if not false
        # anagram string example: "race" anagram of "care"
        # dictorary to track the currently seen elements
        # dict will store the letter and also the count of how many we see, if both dicts same we good
        
        dictS = {}
        dictT = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if dictS.get(s[i]) is None:
                dictS[s[i]] = 1
            dictS[s[i]] = 1 + dictS.get(s[i])
            if dictT.get(t[i]) is None:
                dictT[t[i]] = 1
            dictT[t[i]] = 1 + dictT.get(t[i])

        for count in dictS:
            if dictS[count] != dictT.get(count,0):
                return False
        
        return True
            
                
        
                

