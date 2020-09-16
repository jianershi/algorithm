"""
859. Max Stack
https://www.lintcode.com/problem/max-stack/
九章算法班2020

"""
import heapq
class MaxStack:
    
    def __init__(self):
        # do intialization if necessary
        self.stack = []
        self.max_heap = []
        self.deleted = set()
        self.id = 0
    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, x): #O(logn)
        # write your code here
        item = (-x, -self.id)
        self.stack.append(item)
        heapq.heappush(self.max_heap, item)
        self.id += 1

    """
    @return: An integer
    """
    def pop(self): #O(logn)
        # write your code here
        self.clean_up_stack()
        if self.stack:
            top = self.stack.pop()
            self.deleted.add(top)
        return -top[0]

    """
    @return: An integer
    """
    def top(self): #O(1)
        # write your code here
        self.clean_up_stack()
        if len(self.stack) > 0:
            return -self.stack[-1][0]

    """
    @return: An integer
    """
    def peekMax(self): #O(logn)
        # write your code here
        self.clean_up_heap()
        if self.max_heap:
            max_val, _ = self.max_heap[0]
            return -max_val

    """
    @return: An integer
    """
    def popMax(self): #O(logn)
        # write your code here
        self.clean_up_heap()
        if self.max_heap:
            top = heapq.heappop(self.max_heap)
            self.deleted.add(top)
            return -top[0]

    def clean_up_stack(self):
        while self.stack and self.stack[-1] in self.deleted:
            self.deleted.remove(self.stack.pop())

    def clean_up_heap(self):
        while self.max_heap and self.max_heap[0] in self.deleted:
            self.deleted.remove(heapq.heappop(self.max_heap))
