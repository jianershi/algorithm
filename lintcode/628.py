"""
628. Maximum Subtree
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
    @return: the maximum weight node
    """
    def findSubtree(self, root):
        # write your code here
        if not root:
            return root
        _, _, max_sum_node = self.dfs(root)
        return max_sum_node
    """
    dfs
    @param: root:root of the tree
    @returns: (sum, max_sum, max_sum_node)
                sum is to calculate current level's sum.
                for the leafs, still go to left and right which are empty.
                each side will return sum of 0, with maximum sum of -inf.
                at leaf, it will decide the root has smallest the sum.
                and returns the leaf.
    """
    def dfs(self, root):
        if not root:
            return 0, -sys.maxsize, None

        left_sum, left_max_sum, left_max_sum_node = self.dfs(root.left)
        right_sum, right_max_sum, right_max_sum_node = self.dfs(root.right)
        current_node_sum = left_sum + right_sum + root.val
        max_sum = max(left_max_sum, right_max_sum, current_node_sum)

        if left_max_sum == max_sum:
            return current_node_sum, max_sum, left_max_sum_node
        if right_max_sum == max_sum:
            return current_node_sum, max_sum, right_max_sum_node
        return current_node_sum, max_sum, root
