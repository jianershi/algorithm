"""
94. Binary Tree Maximum Path Sum
https://www.lintcode.com/problem/binary-tree-maximum-path-sum/description
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
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxPathSum(self, root):
        # write your code here
        max_path_sum, max_chain_sum = self.max_path_sum_dfs(root)
        return max_path_sum

    def max_path_sum_dfs(self, root):
        if not root:
            return -sys.maxsize, 0

        max_left_path_sum, max_left_chain_sum = self.max_path_sum_dfs(root.left)
        max_right_path_sum, max_right_chain_sum = self.max_path_sum_dfs(root.right)

        max_path_sum = max(max_left_path_sum, max_right_path_sum, max_left_chain_sum + max_right_chain_sum + root.val)

        max_chain_sum = max(max(max_left_chain_sum, max_right_chain_sum) + root.val, 0)

        return max_path_sum, max_chain_sum
