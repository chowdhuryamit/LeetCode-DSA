# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self,curr,prev):
        if(curr==None):
            return prev
        nxt=curr.next
        curr.next=prev
        prev=curr
        curr=self.solve(nxt,prev)
        return curr    
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev=None
        curr=head
        newhead=self.solve(curr,prev)
        return newhead
        
