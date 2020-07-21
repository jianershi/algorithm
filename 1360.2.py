"""
1360. Symmetric Tree
https://www.lintcode.com/problem/symmetric-tree/description?_from=ladder&&fromId=152

recursive, divide and conquer.
left.right = right.left
left.left = right.right
"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
from collections import deque
class Solution:
    """
    @param root: root of the given tree
    @return: whether it is a mirror of itself 
    """
    def isSymmetric(self, root):
        # Write your code here
        if not root:
            return True
        return self.is_symmetric(root.left, root.right)
        
    def is_symmetric(self, left, right):
        if not left and right:
            return False
        if not right and left:
            return False
            
        if not left and not right:
            return True
        
        if left.val != right.val:
            return False
            
        return self.is_symmetric(left.right, right.left) and self.is_symmetric(left.left, right.right)