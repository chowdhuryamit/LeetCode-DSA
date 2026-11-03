# 219. Contains Duplicate II
# https://leetcode.com/problems/contains-duplicate-ii/

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        m = {}
        for i in range(0,len(nums)):
            if(nums[i] in m and i-m[nums[i]]<=k):
                return True
            else:
                m[nums[i]]=i;    
        return False
        
