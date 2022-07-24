"""
103. Binary Tree Zigzag Level Order Traversal
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        if not root:
            return res
        
        queue = deque([root])
        isFlipped = False
        
        while queue:
            level = []
            for _ in range(len(queue)):
                top = queue.popleft()
                level.append(top.val)
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)
            res.append(level if not isFlipped else level[::-1])
            isFlipped = not isFlipped
        
        return res
        