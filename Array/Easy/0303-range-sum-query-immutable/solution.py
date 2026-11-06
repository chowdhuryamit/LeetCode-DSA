# 303. Range Sum Query - Immutable
# https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        

    def sumRange(self, left: int, right: int) -> int:
        totalSum = 0
        for i in range(left,right+1):
            totalSum+= self.nums[i]
        return totalSum    

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
