# 1385. Find the Distance Value Between Two Arrays
# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/

def isNumExist(arr2, leftNum, rightNum):
    left,right = 0,len(arr2)-1
    while(left<=right):
        mid = int(left+(right-left)/2)
        if(arr2[mid]>=leftNum and arr2[mid]<=rightNum):
            return True
        elif(arr2[mid]<leftNum):
            left=mid+1
        else:
            right=mid-1
    return False   

class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        dist = 0
        arr2.sort()
        for num in arr1:
            leftNum,rightNum = num-d,num+d
            if( not isNumExist(arr2,leftNum,rightNum)):
                dist+=1
        return dist        

