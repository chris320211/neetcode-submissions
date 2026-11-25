#include <iostream>
#include <vector>
#include <string>
#include <map>
// map charcount array of 26 to list of anagrams
// for each string in string we have a list for char count
// for each char, we update the ord
class Solution {
    public:
        std::vector<std::vector<std::string>> groupAnagrams(const std::vector<string>& strs) {
            std::map<std::vector<int>, std::vector<std::string>> map;
            for (const std::string& word : strs) {
                std::vector<int> charCount(26, 0);
                for (const char c : word) {
                    charCount[c - 'a']++;
                }
                map[charCount].push_back(word);
            }
            std::vector<std::vector<std::string>> result;
            result.reserve(strs.size());
            for (auto& p : map) {
                result.push_back(p.second);
            }
            return result;
        }
};
