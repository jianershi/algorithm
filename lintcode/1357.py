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
        self.dfs(root, root.val, [root], sum, result)
        return result
        
    def dfs(self, root, curr, path, target, result):
        if root is None:
            return
        
        if curr > target:
            return
        
        if curr == target:
            result.append([x.val for x in path])
            return
        
        if root.left:
            path.append(root.left)
            self.dfs(root.left, curr + root.left.val, path, target, result)
            path.pop()
        
        if root.right:
            path.append(root.right)
            self.dfs(root.right, curr + root.right.val, path, target, result)
            path.pop()
        