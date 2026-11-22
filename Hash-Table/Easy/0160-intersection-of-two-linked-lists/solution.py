# 160. Intersection of Two Linked Lists
# https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        firstList={}
        temp=headA
        while(temp!=None):
            firstList[temp]=True
            temp=temp.next
        temp=headB
        while(temp!=None):
            if(firstList.get(temp)):
                return temp
            else:
                temp=temp.next
        return None                
        
