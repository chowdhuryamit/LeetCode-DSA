# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if(head==None):
            return None
        if(head.next==None):
            return head
        else:
            prev=head
            curr=head.next
            nxt=curr.next
            while(curr):
                curr.next=prev
                prev=curr
                curr=nxt
                if(nxt!=None):
                    nxt=nxt.next
            head.next=None
            return prev                
        
