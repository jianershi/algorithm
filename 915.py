"""
915. Inorder Predecessor in BST
https://www.lintcode.com/problem/inorder-predecessor-in-bst/description
九章高频题班
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
    @param root: the given BST
    @param p: the given node
    @return: the in-order predecessor of the given node in the BST
    """
    def inorderPredecessor(self, root, p):
        # write your code here
        if not root:
            return None

        c1 = p.left
        ans = c1
        while c1:
            ans = c1
            c1 = c1.right

        prev_father = None

        while root != p:
            if p.val < root.val:
                root = root.left
            else:
                prev_father = root
                root = root.right

        return ans or prev_father
