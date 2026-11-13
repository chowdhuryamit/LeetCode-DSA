# 643. Maximum Average Subarray I
# https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        windowSum=0
        left=0
        maxAvg=float("-inf")
        for i in range(0,k):
            windowSum+=nums[i]    
        maxAvg=max(maxAvg,windowSum/k)    
        for i in range(k,len(nums)):
            windowSum+=nums[i]
            windowSum-=nums[left]
            left+=1
            maxAvg=max(maxAvg,windowSum/k)
        return maxAvg    

        
