"""
86. Binary Search Tree Iterator
https://www.lintcode.com/problem/binary-search-tree-iterator/description

the difference between this method and the standard method is:
if one has right subtree, it no longer keep itself in the stack.
so when taken out of the stack, it does not need to make extra step to remove itself.

the downside of this simplified method is it is not appliable to find
kth closest member in a binary tree (maybe?)
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
        self.root = root
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    """
    @return: True if there has next node, or false
    """
    def hasNext(self):
        # write your code here
        return len(self.stack) > 0

    """
    @return: return next node
    """
    def next(self):
        # write your code here
        if not self.hasNext():
            return None

        node = self.stack.pop()

        p = node.right
        while p:
            self.stack.append(p)
            p = p.left

        return node
