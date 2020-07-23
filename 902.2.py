"""
902. Kth Smallest Element in a BST
https://www.lintcode.com/problem/kth-smallest-element-in-a-bst/description?_from=ladder&&fromId=37
divide and conquer
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
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        # write your code here
        count, kth = self.dfs(root,k)
        return kth.val

    """
    left tree count, left found
    right tree count, right found
    """
    def dfs(self, root, k):
        if not root:
            return 0, None

        left_count, left_found = self.dfs(root.left, k)
        right_count, right_found = self.dfs(root.right, k - left_count - 1)
        
        if left_count >= k:
            return left_count + right_count + 1, left_found
        if left_count + 1 == k:
            return left_count + right_count + 1, root
        if left_count + right_count + 1 >= k:
            return left_count + right_count + 1, right_found
        
        return left_count + right_count + 1, None
