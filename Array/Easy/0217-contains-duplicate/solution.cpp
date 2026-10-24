// 217. Contains Duplicate
// https://leetcode.com/problems/contains-duplicate/

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        bool isDuplicate= false;
        for(int i=1;i<nums.size();i++){
            if(nums[i]==nums[i-1]){
                isDuplicate=true;
                break;
            }
        }
        return isDuplicate;
    }
};
