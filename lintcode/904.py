"""
904. Plus One Linked List
use recursion
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
    @param head: the first Node
    @return: the answer after plus one
    """
    def plusOne(self, head):
        # Write your code here

        r = self.plusOneHelper(head)
        dummy = head
        if r:
            dummy = ListNode(1)
            dummy.next = head
        return dummy

    def plusOneHelper(self, head):
        if head is None:
            return 1

        if self.plusOneHelper(head.next):
            if head.val + 1 > 9:
                head.val = 0
                return 1
            else:
                head.val += 1
                return 0
