"""
126. Max Tree
https://www.lintcode.com/problem/max-tree/description
令老师的解答： https://www.jiuzhang.com/solution/max-tree/
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
        stack = []
        n = len(A)

        top = None

        nodes = [TreeNode(x) for x in A + [sys.maxsize]]
        for i in range(n + 1):
            curr_node = sys.maxsize if i == n else A[i]
            while stack and curr_node >= A[stack[-1]]:
                top = stack.pop()
                left = A[stack[-1]] if stack else sys.maxsize
                right = curr_node
                if left < right:
                    nodes[stack[-1]].right = nodes[top]
                else:
                    nodes[i].left = nodes[top]

            stack.append(i)

        return nodes[top] #the last element to pop is the root of the tree
