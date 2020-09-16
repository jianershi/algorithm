"""
221. Add Two Numbers II
Input: 6->1->7   2->9->5
Output: 9->1->2

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
    @param l1: The first list.
    @param l2: The second list.
    @return: the sum list of l1 and l2.
    """
    def addLists2(self, l1, l2):
        # write your code here
        num1 = self.get_number(l1)
        num2 = self.get_number(l2)
        sum = num1 + num2

        return self.create_linked_list(sum)

    def get_number(self, head):
        num = 0
        while head:
            num = num * 10 + head.val
            head = head.next
        return num
        """
        1->2->null
        0*10+1 = 1
        1*10+2 = 12
        """

    def create_linked_list(self, sum):
        dummy = ListNode(0)
        tail = dummy
        sum_str = str(sum)
        while sum_str:
            tail.next = ListNode(int(sum_str[0]))
            sum_str = sum_str[1:]
            tail = tail.next

        return dummy.next
