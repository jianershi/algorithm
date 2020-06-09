"""
174. Remove Nth Node From End of List

https://www.lintcode.com/problem/remove-nth-node-from-end-of-list/
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
    @param head: The first node of linked list.
    @param n: An integer
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        # write your code here
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy
        for _ in range(n + 1):
            if fast == None:
                return head
            fast = fast.next

        while fast!= None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next
