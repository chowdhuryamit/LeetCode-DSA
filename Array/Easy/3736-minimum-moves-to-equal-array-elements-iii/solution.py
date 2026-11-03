# 3736. Minimum Moves to Equal Array Elements III
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        num = nums[len(nums)-1]
        move = 0
        for number in nums:
            move+=num-number
        return move
        
