"""
126. Max Tree
https://www.lintcode.com/problem/max-tree/description
"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import sys
class Solution:
    """
    @param A: Given an integer array with no duplicates.
    @return: The root of max tree.
    """
    def maxTree(self, A):
        # write your code here
        map = {} # value: node
        stack = []
        n = len(A)

        center = None
        for i in range(n + 1):
            curr_node = sys.maxsize if i == n else A[i]
            while stack and curr_node >= A[stack[-1]]:
                center = stack.pop()
                left = A[stack[-1]] if stack else sys.maxsize
                right = curr_node
                if left < right:
                    map[left] = map.get(left, TreeNode(left))
                    map[left].right = map.get(A[center], TreeNode(A[center]))
                else:
                    map[right] = map.get(right, TreeNode(right))
                    map[right].left = map.get(A[center], TreeNode(A[center]))

            stack.append(i)

        return map.get(A[center], TreeNode(A[center]))
