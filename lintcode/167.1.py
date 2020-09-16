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
        s1 = []
        s2 = []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        
        a1 = a2 = 0
        while s1:
            a1 = 10 * a1 + s1.pop()
        while s2:
            a2 = 10 * a2 + s2.pop()
        
        s = str(a1 + a2)[::-1]
        
        dummy = ListNode(0)
        tail = dummy
        
        for digit in s:
            tail.next = ListNode(digit)
            tail = tail.next
        
        return dummy.next
            
