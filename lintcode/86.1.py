"""
86. Binary Search Tree Iterator
https://www.lintcode.com/problem/binary-search-tree-iterator/description
"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node 
"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node 
"""
class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        # do intialization if necessary
        self.stack = []
        p = root
        while p is not None:
            self.stack.append(p)
            p = p.left

    """
    @return: True if there has next node, or false
    """
    def hasNext(self, ):
        # write your code here
        return len(self.stack) > 0

    """
    @return: return next node
    """
    def next(self, ):
        # write your code here
        curr = self.stack[-1]
        if curr.right is not None:
            node = curr.right
            while node is not None:
                self.stack.append(node)
                node = node.left
        else:
            node = self.stack.pop()
            while self.stack and self.stack[-1].right is node:
                node = self.stack.pop()
                
        return curr