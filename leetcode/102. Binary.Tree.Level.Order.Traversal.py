"""
102. Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        queue = collections.deque([(root)])
        visited = set()
        lot = []
        while queue:
            level = []
            for _ in range(len(queue)):
                top = queue.popleft()
                level.append(top.val)
                if top.left and top.left not in visited:
                    queue.append(top.left)
                    visited.add(top.left)
                if top.right and top.right not in visited:
                    queue.append(top.right)
                    visited.add(top.right)
            lot.append(level)
        return lot