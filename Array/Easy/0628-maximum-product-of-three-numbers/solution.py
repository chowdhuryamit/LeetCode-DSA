# 628. Maximum Product of Three Numbers
# https://leetcode.com/problems/maximum-product-of-three-numbers/

class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        nums.sort()
        size=len(nums)
        if(len(nums)==3):
            return nums[0]*nums[1]*nums[2]
        else:
            ans1=nums[size-1]*nums[size-2]*nums[size-3]
            ans2=nums[0]*nums[1]*nums[2]
            ans3=nums[0]*nums[1]*nums[size-1]
            return max(ans1,ans2,ans3)
        
