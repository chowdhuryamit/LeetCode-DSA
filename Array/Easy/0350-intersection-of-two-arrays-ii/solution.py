# 350. Intersection of Two Arrays II
# https://leetcode.com/problems/intersection-of-two-arrays-ii/

def isPresent(num,nums2):
    left,right = 0,len(nums2)-1
    nums2.sort()
    while(left<=right):
        mid = int(left+(right-left)/2)
        if(nums2[mid] == num):
            nums2[mid]=-1
            return True
        elif(nums2[mid]>num):
            right = mid-1
        else:
            left = mid+1
    return False                
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans = []
        nums2.sort()
        for num in nums1:
            if(isPresent(num,nums2)):
                ans.append(num)
        return ans        
        
