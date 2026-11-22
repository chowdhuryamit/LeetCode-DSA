# 141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if(head==None):
            return False
        visitedNode={}
        temp=head
        visitedNode[temp]=True
        temp=temp.next
        while(temp!=None):
            if(visitedNode.get(temp)):
                return True
            else:
                visitedNode[temp]=True
                temp=temp.next
        return False            

        
