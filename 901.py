"""
901. Closest Binary Search Tree Value II

https://www.lintcode.com/problem/closest-binary-search-tree-value-ii/description
"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
"""
方案一：
"""
class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """
    def closestKValues(self, root, target, k):
        # write your code here
        """
        1.先在二叉树内找target, 这个步骤花费O(h). 往左寻找表示target比当前节点小。这个全部记录在next_bigger_stack。
        当target > root的时候，就要往右子树寻找，这个时候的点存在next_smaller_stack里面。存完以后，这两个stack里面的值一定是离target由远到近的。因此离target最近的点一定是栈顶。之后只需要按照这个栈去iterate下一个点就可以了。
        2.这个时候要用到的iterator和BST的相似。next_bigger_stack里面的点相当于inordertraversal, 只要按照inorder traversal 的iterate去写就好了。而往next_smaller_stack相当于一个反过来的iterate,完全和前面的iterate是镜像。
        """
        result = []
        if root is None or k == 0:
            return result

        next_bigger_stack, next_smaller_stack = self.build_stack(root, target)


        while len(result) < k:
            next_bigger_diff = next_bigger_stack[-1].val - target if len(next_bigger_stack) else sys.maxsize
            next_smaller_diff = target - next_smaller_stack[-1].val if len(next_smaller_stack) else sys.maxsize

            if next_bigger_diff < next_smaller_diff:
                result.append(self.find_next_bigger_number(next_bigger_stack))
            else:
                result.append(self.find_next_smaller_number(next_smaller_stack))

        return result


    def build_stack(self, root, target):
        next_bigger_stack = []
        next_smaller_stack = []
        while root:
            if target < root.val:
                next_bigger_stack.append(root)
                root = root.left
            else:
                next_smaller_stack.append(root)
                root = root.right
        return next_bigger_stack, next_smaller_stack

    def find_next_bigger_number(self, next_bigger_stack):
        if not next_bigger_stack:
            return None
        node = next_bigger_stack.pop()
        n = node.right
        while n:
            next_bigger_stack.append(n)
            n = n.left
        return node.val

    def find_next_smaller_number(self, next_smaller_stack):
        if not next_smaller_stack:
            return None
        node = next_smaller_stack.pop()
        n = node.left
        while n:
            next_smaller_stack.append(n)
            n = n.right
        return node.val
