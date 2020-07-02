"""
22. Flatten List
https://www.lintcode.com/problem/flatten-list/description

non recursion
"""
from collections import deque
class Solution(object):

    # @param nestedList a list, each element in the list 
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        # Write your code here
        stack = deque([nestedList])
        result = []
        while queue:
            front = stack.popleft()
            if isinstance(front, int):
                result.append(front)
            else:
                for sub_item in front:
                    queue.appendleft(sub_item)
        return result
