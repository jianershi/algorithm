"""
35. Reverse Linked List
https://www.lintcode.com/problem/reverse-linked-list/description?_from=ladder&&fromId=37
"""
"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        # write your code here
        if not head:
            return head
        now_p = head
        prev_p = None
        
        while now_p:
            next_p = now_p.next
            now_p.next = prev_p
            prev_p = now_p
            now_p = next_p
            
        return prev_p
            
            
            