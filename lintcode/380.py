"""
380. Intersection of Two Linked Lists
https://www.lintcode.com/problem/intersection-of-two-linked-lists/description
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
    @param headA: the first list
    @param headB: the second list
    @return: a ListNode
    """
    def getIntersectionNode(self, headA, headB):
        # write your code here
        if not headA or not headB:
            return None

        p1 = headA
        while p1.next:
            p1 = p1.next
        p1.next = headB


        slow, fast = headA, headA
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break

        slow = headA
        while slow != fast:
            fast = fast.next
            slow = slow.next

        p1.next = None

        return slow
