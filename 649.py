"""
649. Binary Tree Upside Down
https://www.lintcode.com/problem/binary-tree-upside-down/description
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
    @param root: the root of binary tree
    @return: new root
    """
    def upsideDownBinaryTree(self, root):
        # write your code here
        root, _ = self.flip(root)
        return root

    def flip(self, root):
        if not root: #处理原始数据传进来就是空的情况
            return root, root
        if not root.left and not root.right:
            return root, root

        new_root, right_leaf = self.flip(root.left)
        right_leaf.left = root.right
        right_leaf.right = root
        root.right = None
        root.left = None
        return new_root, root
