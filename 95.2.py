"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        # write your code here
        # self.last_node = None
        last_node = None
        isBST, last_node = self.inorder_traversal(root, last_node)
        return isBST

    """
    using in order traversal.
    只需要记录最后一个node的值
    """
    def inorder_traversal(self, node, last_node):
        if not node:
            return True, last_node

        isBST, last_node = self.inorder_traversal(node.left, last_node)

        if last_node and node.val <= last_node.val:
            isBST = False
            return isBST, last_node
        else:
            last_node = node
        isBST, last_node = self.inorder_traversal(node.right, last_node)

        return isBST, last_node

def main():
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(1)
    print(s.isValidBST(root))


if __name__=="__main__":
    main()
