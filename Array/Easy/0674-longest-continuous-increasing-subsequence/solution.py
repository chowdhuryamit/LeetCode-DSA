# 674. Longest Continuous Increasing Subsequence
# https://leetcode.com/problems/longest-continuous-increasing-subsequence/

class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        localLength=1
        ans=1
        for i in range(1,len(nums)):
            if(nums[i]>nums[i-1]):
                localLength+=1
            else:
                ans=max(ans,localLength)
                localLength=1    
        ans=max(ans,localLength)
        return ans        
