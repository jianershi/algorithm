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
from collections import deque
class Solution:
    """
    @param l1: the first list
    @param l2: the second list
    @return: the sum list of l1 and l2 
    """
    def addLists(self, l1, l2):
        # write your code here
        s1 = []
        s2 = []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next

        s = []
        carry = 0
        i, j = 0, 0
        while i <= len(s1) - 1 or j <= len(s2) - 1:
            if i >= len(s1):
                p1 = 0
            if j >= len(s2):
                p2 = 0
            if i < len(s1):
                p1 = s1[i]
                i += 1
            if j < len(s2):
                p2 = s2[j]
                j += 1
            
            s.append((p1 + p2 + carry) % 10)
            carry = (p1 + p2 + carry) // 10
        
        if carry:
            s.append(carry)
            
        dummy = ListNode(0)
        tail = dummy
        
        for digit in s:
            tail.next = ListNode(digit)
            tail = tail.next
        
        return dummy.next
            
