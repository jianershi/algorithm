"""
1360. Symmetric Tree
https://www.lintcode.com/problem/symmetric-tree/description?_from=ladder&&fromId=152

bfs level order travelsal + palindrome/2pointer
"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
from collections import deque
class Solution:
    """
    @param root: root of the given tree
    @return: whether it is a mirror of itself 
    """
    def isSymmetric(self, root):
        # Write your code here
        q = deque([root])
        
        while q:
            level = []
            for _ in range(len(q)):
                f = q.popleft()
                if not f:
                    level.append(f)
                if f:
                    level.append(f.val)
                    q.append(f.left)
                    q.append(f.right)
                
            for i in range(len(level)):
                if level[i] != level[len(level) - 1 - i]:
                    return False
        return True