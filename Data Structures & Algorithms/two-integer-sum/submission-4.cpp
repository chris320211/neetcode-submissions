// hashmap to track of the difference 
// return idexes
// hashmap difference -> i
// if difference we need to reach target is there retrun i
#include <iostream>
#include <unordered_map>
#include <vector>
class Solution{
    public:
        vector<int> twoSum(const std::vector<int>& nums, int& target) {
            std::unordered_map<int, int> map;
            for (int i = 0; i < nums.size(); i++) {
                if (map.contains(nums[i])) {
                    return {map[nums[i]], i};
                }
                map[target - nums[i]] = i;
            }
        }
};
