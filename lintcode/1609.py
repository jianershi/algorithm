"""
1609. Middle of the Linked List

https://www.lintcode.com/problem/middle-of-the-linked-list/note
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
    @param head: the head node
    @return: the middle node
    """
    def middleNode(self, head):
        # write your code here.
        fast = head
        slow = head
        count = 0
        while fast!= None:
            fast = fast.next
            if count % 2:
                slow = slow.next
            count += 1
        return slow
