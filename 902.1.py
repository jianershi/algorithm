"""
902. Kth Smallest Element in a BST
https://www.lintcode.com/problem/kth-smallest-element-in-a-bst/description?_from=ladder&&fromId=37

using bst iterator
refer to 86.standard.py
"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class BSTIterator:
    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left
                
        
    def next(self):
        curr = self.stack[-1]
        if curr.right:
            node = curr.right
            while node:
                self.stack.append(node)
                node = node.left

        else:
            top = self.stack.pop()
            while self.stack and self.stack[-1].right is top:
                top = self.stack.pop()

        return curr

class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        # write your code here
        it = BSTIterator(root)
        for _ in range(k):
            ret = it.next()
        return ret.val
