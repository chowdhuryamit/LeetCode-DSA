# 83. Remove Duplicates from Sorted List
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        if(head==None):
            return head
        curr=head.next
        prev=head
        while(curr!=None):
            if(curr.val>prev.val):
                prev=curr
                curr=curr.next
            else:
                prev.next=curr.next
                curr=curr.next
        return head            

        
