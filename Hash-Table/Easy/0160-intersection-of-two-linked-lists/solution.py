# 160. Intersection of Two Linked Lists
# https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lengthA,lengthB=0,0
        temp=headA
        while(temp!=None):
            lengthA+=1
            temp=temp.next
        temp=headB
        while(temp!=None):
            lengthB+=1
            temp=temp.next
        tempA,tempB=headA,headB
        if(lengthA>lengthB):
            diff=lengthA-lengthB
            while(diff):
                tempA=tempA.next
                diff-=1
        else:
            diff=lengthB-lengthA
            while(diff):
                tempB=tempB.next
                diff-=1
        while(tempA!=None and tempB!=None):
            if(tempA==tempB):
                return tempA
            else:
                tempA=tempA.next
                tempB=tempB.next
        return None                               
