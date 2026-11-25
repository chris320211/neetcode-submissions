#include <iostream>
#include <unordered_set>
#include <vector>

class Solution {
public:
    bool hasDuplicate(const std::vector<int>& nums) {
        // interger array nums
        // return true if any value appears more than once
        std::unordered_set<int> s;
        s.reserve(nums.size());
        for (int n : nums) {
            if (!s.insert(n).second) {
                return true;
            }
        }
        return false;
    }
};