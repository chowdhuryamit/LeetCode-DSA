// 1. Two Sum
// https://leetcode.com/problems/two-sum/

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> m;
        m[nums[0]] = 0;
        for (int i = 1; i < nums.size(); i++) {
            int required = target - nums[i];
            auto it = m.find(required);
            if (it != m.end()) {
                return {it->second, i};
            }
            m[nums[i]] = i;
        }
        return {-1, -1};
    }
};
