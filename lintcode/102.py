"""
102. Linked List Cycle
https://www.lintcode.com/problem/linked-list-cycle/description
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
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        # write your code here
        if head == None or head.next == None:
            return False

        slow, fast = head, head.next
        while fast != None:
            fast = fast.next
            if fast != None:
                fast = fast. next
            slow = slow.next
            if slow == fast:
                return True
        return False
