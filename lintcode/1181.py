"""
1181. Diameter of Binary Tree
https://www.lintcode.com/problem/diameter-of-binary-tree/description
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
    @param root: a root of binary tree
    @return: return a integer
    """
    def diameterOfBinaryTree(self, root):
        # write your code here
        m_d, _ = self.dfs(root)
        return m_d

    def dfs(self, root):
        if not root:
            return 0, 0
        left_m_d, left_m_c = self.dfs(root.left)
        right_m_d, right_m_c = self.dfs(root.right)

        m_d = max(left_m_d, right_m_d, left_m_c + right_m_c)
        m_c = max(left_m_c, right_m_c) + 1

        return m_d, m_c
