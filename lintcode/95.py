"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        # write your code here
        minimum = None
        maximum = None
        isBST, minimum_left, minimum_right = self.check_node(root, minimum, maximum)
        return isBST


    def check_node(self, root, minimum, maximum):
        if not root:
            return True, 0, 0

        isBST_left, minimum_left, maximum_left = self.check_node(root.left, minimum, maximum)
        isBST_right, minimum_right, maximum_right = self.check_node(root.right, minimum, maximum)

        if not isBST_left or not isBST_right:
            return False, 0, 0
        if root.left and maximum_left >= root.val:
            return False, 0, 0
        if root.right and minimum_right <= root.val:
            return False, 0, 0

        #isBST
        return True, minimum_left if minimum_left else root.val, maximum_right if maximum_right else root.val
