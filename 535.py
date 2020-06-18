"""
535. House Robber III
https://www.lintcode.com/problem/house-robber-iii/
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
    @param root: The root of binary tree.
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber3(self, root):
        # write your code here
        m_not_in_p, m_in_p = self.dfs(root)
        return max(m_not_in_p, m_in_p)

    def dfs(self, root):
        if not root:
            return 0, 0

        m_not_in_p_left, m_in_p_left = self.dfs(root.left)
        m_not_in_p_right, m_in_p_right = self.dfs(root.right)

        m_in_p = m_not_in_p_left + m_not_in_p_right + root.val

        m_not_in_p = max(m_not_in_p_left, m_in_p_left) + max(m_not_in_p_right, m_in_p_right)

        return m_not_in_p, m_in_p
