// given two string
// return true if anagram
// return true if hashmaps are equal

#include <iostream>
#include <string>
#include <unordered_map>

class Solution {
public:
    bool isAnagram(const std::string& s, const std::string& t) {
        if (s.length() != t.length()) {
            return false;
        }
        std::unordered_map<char, int> sMap;
        std::unordered_map<char, int> tMap;
        for (int i = 0; i < s.size(); i++) {
            sMap[s[i]]++;
            tMap[t[i]]++;
        }
        return sMap == tMap;
    }
};
