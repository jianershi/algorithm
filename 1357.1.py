"""
1357. Path Sum II
https://www.lintcode.com/problem/path-sum-ii/description?_from=ladder&&fromId=131
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
    @param root: a binary tree
    @param sum: the sum
    @return: the scheme
    """
    def pathSum(self, root, sum):
        # Write your code here.
        result = []
        if not root:
            return []
        self.dfs(root, 0, [], sum, result)
        return result
        
    def dfs(self, root, curr, path, target, result):
        if root is None:
            return
        
        if curr + root.val > target:
            return
        
        if curr + root.val == target:
            result.append([x.val for x in path] + [root.val])
            return
        
        path.append(root)
        self.dfs(root.left, curr + root.val, path, target, result)
        self.dfs(root.right, curr + root.val, path, target, result)
        path.pop()
        