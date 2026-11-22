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
        stack=[]
        temp=head
        while(temp!=None):
            stack.append(temp)
            temp=temp.next  
        head=stack[-1]
        stack.pop()
        temp=head
        while(stack):
            temp.next=stack[-1]
            stack.pop()
            temp=temp.next
        temp.next=None    
        return head


        
