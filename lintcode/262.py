"""
262. heir tree
https://www.lintcode.com/problem/heir-tree/description?_from=ladder&&fromId=160
九章高频课
这道题。。其实蛮简单的。。只要注意。一个人继承权消失以后并不会影响子女的继承权和其他继承顺序。
所以这里实际上是不能删的。用了lazy delete的思想。（其实并没有delete就对了）
"""
class MyTreeNode:
    """
    @param val: the node's val
    @return: a MyTreeNode object
    """
    def __init__(self, val):
        # write your code here
        self.val = val
        self.children = []
        self.deleted = False

    """
    @param root: the root treenode
    @return: get the traverse of the treenode
    """
    def traverse(self, root):
        # write your code here
        results = []
        self.traverse_dfs(root, results)
        return results

    def traverse_dfs(self, root, results):
        if not root.deleted:
            results.append(root.val)

        for child in root.children:
            self.traverse_dfs(child, results)
    """
    @param root: the node where added
    @param value: the added node's value
    @return: add a node, return the node
    """
    def addNode(self, root, value):
        # write your code here
        child = MyTreeNode(value)
        root.children.append(child)
        return child

    """
    @param root: the deleted node
    @return: nothing
    """
    def deleteNode(self, root):
        # write your code here
        root.deleted = True
