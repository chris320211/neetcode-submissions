#include <iostream>
#include <set>
#include <vector>

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        // interger array nums
        // return true if any value appears more than once
        std::set<int> s;
        for (int n : nums) {
            if (s.contains(n)) {
                return true;
            }
            s.insert(n);
        }
        return false;
    }
};