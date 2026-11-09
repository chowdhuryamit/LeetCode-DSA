# 599. Minimum Index Sum of Two Lists
# https://leetcode.com/problems/minimum-index-sum-of-two-lists/

class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        dictList1,dictList2={},{}
        dictAns={}
        for i in range(len(list1)-1,-1,-1):
            dictList1[list1[i]]=i
        for i in range(len(list2)-1,-1,-1):
            dictList2[list2[i]]=i
        for key,value in dictList1.items():
            if key in dictList2:
                dictAns[key]=value+dictList2[key]
        minIndexValue=float("inf")      
        for key,value in dictAns.items():
            minIndexValue=min(minIndexValue,value)
        ans=[]
        for key,value in dictAns.items():
            if(value==minIndexValue):
                ans.append(key)
        return ans                 
        
