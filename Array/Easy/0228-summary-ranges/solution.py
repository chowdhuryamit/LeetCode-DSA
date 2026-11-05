# 228. Summary Ranges
# https://leetcode.com/problems/summary-ranges/

class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if (len(nums)==0):
            return []
        ans = []
        localRange = [nums[0]]
        for i in range(1,len(nums)):
            if(nums[i]-1==nums[i-1]):
                localRange.append(nums[i])
            else:
                ans.append(localRange)
                localRange=[]
                localRange.append(nums[i])    
        ans.append(localRange)
        for i in range(0,len(ans)):
            if(len(ans[i])>1):
                ans[i]=str(ans[i][0])+"->"+str(ans[i][len(ans[i])-1])
            else:
                ans[i]=str(ans[i][0])    
        return ans

        
