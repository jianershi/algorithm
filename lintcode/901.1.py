"""
901. Closest Binary Search Tree Value II
https://www.lintcode.com/problem/closest-binary-search-tree-value-ii/description

first, have to use BST search to find the target. path recorded every move to get to the target
then make 2 iterator one go higher one go lower
then compare which one is closer

这个写法更加通用。用了令狐冲老师的写法。这样iterator是可以遍历所有往前和往后的节点的。
而另外一种写法里，一旦去了一个节点的右子树，这个节点就被抛弃了。通用性没那么好。而且在
建stack过程中方法也不一样。这个方法等于是用在BST中找元素的方法把寻找路径记了下来。
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
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """
    def build_stack(self, root, target):
        stack = []
        while root:
            stack.append(root)
            if root.val < target:
                root = root.right
            else:
                root = root.left
        return stack

    def closestKValues(self, root, target, k):
        if not root or k == 0:
            return []

        upper_stack = self.build_stack(root, target)
        lower_stack = list(upper_stack)

        if upper_stack and upper_stack[-1].val < target: #we don't know the last node in the queue is bigger or smaller
            self.next(upper_stack)
        else:
            self.prev(lower_stack)

        results = []
        for _ in range(k):
            if self.is_lower_smaller(lower_stack, upper_stack, target):
                print (lower_stack[-1].val)
                results.append(lower_stack[-1].val)
                self.prev(lower_stack)
            else:
                print (upper_stack[-1].val)
                results.append(upper_stack[-1].val)
                self.next(upper_stack)

        return results

    def is_lower_smaller(self, lower, upper, target):
        if not lower:
            return False
        if not upper:
            return True
        return target - lower[-1].val < upper[-1].val - target

    def next(self, stack):
        if not stack:
            return None
        node = stack[-1]

        if node.right:
            n = node.right
            while n:
                stack.append(n)
                n = n.left
        else:
            n = stack.pop()
            while stack and stack[-1].right == n:
                n = stack.pop()

        return node

    def prev(self, stack):
        if not stack:
            return None
        node = stack[-1]

        if node.left:
            n = node.left
            while n:
                stack.append(n)
                n = n.right
        else:
            n = stack.pop()
            while stack and stack[-1].left == n:
                n = stack.pop()

        return node
