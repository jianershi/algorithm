"""
859. Max Stack
https://www.lintcode.com/problem/max-stack/
九章算法班2020

worst case O(n) for popMax if the maximum number is at the beginning,
for example. [5, 4, 3, 2, 1]
"""
class MaxStack:
    
    def __init__(self):
        # do intialization if necessary
        self.stack = []
        self.max_stack = []
    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, x):
        # write your code here
        self.stack.append(x)
        if len(self.max_stack) == 0 or x > self.max_stack[-1]:
            self.max_stack.append(x)

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        self.max_stack.pop()
        return self.stack.pop()

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        if len(self.stack) > 0:
            return self.stack[-1]

    """
    @return: An integer
    """
    def peekMax(self):
        # write your code here
        if self.max_stack:
            return self.max_stack[-1]

    """
    @return: An integer
    """
    def popMax(self):
        # write your code here
        buffer = []
        while self.stack and self.stack[-1] != self.max_stack[-1]:
            buffer.append(self.stack.pop())
            self.max_stack.pop()
        if len(self.stack) > 0:
            res = self.stack.pop()
        for num in buffer:
            self.push(num)
        return res
