"""
492. Implement Queue by Linked List

https://www.lintcode.com/problem/implement-queue-by-linked-list/description
"""
class LinkedNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyQueue:
    """
    @param: item: An integer
    @return: nothing
    """
    def __init__(self):
        self.dummy = LinkedNode(0)
        self.tail = self.dummy
        self.size = 0

    def enqueue(self, item):
        # write your code here
        self.tail.next = LinkedNode(item)
        self.tail = self.tail.next
        self.size += 1
    """
    @return: An integer
    """
    def dequeue(self):
        # write your code here
        if not self.size:
            return None

        head = self.dummy.next
        self.dummy = self.dummy.next
        self.size -= 1
        return head.val
