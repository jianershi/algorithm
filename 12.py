"""
12. Min Stack
https://www.lintcode.com/problem/min-stack/description
"""
class MinStack:

    def __init__(self):
        # do intialization if necessary
        self.stack = []
        self.min_stack = []
    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, number):
        # write your code here
        self.stack.append(number)
        self.min_stack.append(number if len(self.min_stack) == 0 else min(number, self.min_stack[-1]))

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        self.min_stack.pop()
        return self.stack.pop()

    """
    @return: An integer
    """
    def min(self):
        # write your code here
        return self.min_stack[-1]
