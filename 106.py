"""
106. Convert Sorted List to Binary Search Tree
https://www.lintcode.com/problem/convert-sorted-list-to-binary-search-tree/description
九章高频题班
因为是平衡树编辑的问题，自然想到了分治。
合并操作： 左边变成BST + root + 右边变成BST.
每一层O(1), 总共log(N)曾，所以O(logN), 但是，每一次合并并非O(1), 因为找linkedlist中点就需要O(N),
所以复杂度是 O(NlogN)。这时候就想，有没有办法所幸每次把结束的点传回去，这样我下次直接从那个点开始就好了。
就不需要再搜索中点。所以这边的思想就是。分治法参数不够的时候多传参数就可以了。
"""
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param: head: The first node of linked list.
    @return: a tree node
    """
    def sortedListToBST(self, head):
        # write your code here
        # if not head:
            # return None
        size = self.find_length(head)

        left, mid = self.helper(head, size)
        return left

    def find_length(self, head):
        size = 0
        p = head
        while p:
            size += 1
            p = p.next
        return size

    def helper(self, head, length):
        if length == 0:
            return None, head

        left, mid = self.helper(head, length // 2)
        root = TreeNode(mid.val)
        right, nxt = self.helper(mid.next, length - length // 2 - 1)
        root.left = left
        root.right = right
        return root, nxt
