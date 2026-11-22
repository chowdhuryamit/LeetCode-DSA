# 2124. Check if All A's Appears Before All B's
# https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/

class Solution:
    def checkString(self, s: str) -> bool:
        foundB=False
        for ele in s:
            if(ele=='a'):
                if(foundB==True):
                    return False
            else:
                foundB=True
        return True        
        
