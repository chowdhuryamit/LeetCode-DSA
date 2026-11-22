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
        slowPointer,fastPointer=head,head
        while(fastPointer!=None):
            slowPointer=slowPointer.next
            fastPointer=fastPointer.next
            if(fastPointer!=None):
                fastPointer=fastPointer.next
            if(fastPointer==None):
                break    
            if(slowPointer==fastPointer):
                return True
        return False                


        
