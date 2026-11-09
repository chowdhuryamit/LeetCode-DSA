# 598. Range Addition II
# https://leetcode.com/problems/range-addition-ii/

class Solution:
    def maxCount(self, m: int, n: int, ops: list[list[int]]) -> int:
        ops.sort()
        if(len(ops)!=0):
            minRow,minCol=float("inf"),float("inf")
            for pair in ops:
                minRow=min(minRow,pair[0])
                minCol=min(minCol,pair[1])
            return minRow*minCol    
        else:
            return m*n    
        
