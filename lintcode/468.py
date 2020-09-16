"""
468. Symmetric Binary Tree
https://www.lintcode.com/problem/symmetric-binary-tree/description?_from=ladder&&fromId=131
"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree.
    @return: true if it is a mirror of itself, or false.
    """
    def isSymmetric(self, root):
        # write your code here
        if not root:
            return True
        return self.is_mirror(root.left, root.right)
    
    def is_mirror(self, left, right):
        if not left and not right:
            return True
        
        if not left and right:
            return False
        
        if not right and left:
            return False
            
        if left.val != right.val:
            return False
            
        return self.is_mirror(left.left, right.right) and self.is_mirror(left.right, right.left)