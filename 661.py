"""
661. Convert BST to Greater Tree
https://www.lintcode.com/problem/convert-bst-to-greater-tree
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
    @return: the new root
    """
    def convertBST(self, root):
        # write your code here
        self.travel(root, 0)
        return root

    def travel(self, root, now_sum):
        if not root:
            return now_sum

        now_sum = self.travel(root.right, now_sum)
        now_sum += root.val
        root.val = now_sum
        now_sum = self.travel(root.left, now_sum)

        return now_sum
