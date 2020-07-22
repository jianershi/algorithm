"""
167. Add Two Numbers
https://www.lintcode.com/problem/add-two-numbers/description?_from=ladder&&fromId=37
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
    @param l1: the first list
    @param l2: the second list
    @return: the sum list of l1 and l2 
    """
    def addLists(self, l1, l2):
        # write your code here
        root = ListNode(0)
        tail = root
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            tail.val = carry % 10
            carry //= 10
            if l1 or l2 or carry:
                tail.next = ListNode(0)
                tail = tail.next
        return root