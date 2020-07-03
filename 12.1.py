"""
12. Min Stack
https://www.lintcode.com/problem/min-stack/description

save some space on the min_stack by only pushing replicating numbers onto the min stack
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
        if len(self.min_stack) == 0 or number <= self.min_stack[-1]:
            self.min_stack.append(number)

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        if self.min_stack and self.stack and self.min_stack[-1] == self.stack[-1]:
            self.min_stack.pop()
        
        return self.stack.pop()
    """
    @return: An integer
    """
    def min(self):
        # write your code here
        return self.min_stack[-1]
