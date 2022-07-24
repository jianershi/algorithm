"""
242 · Convert Binary Tree to Linked Lists by Depth
https://www.lintcode.com/problem/242/

Description
Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        # Write your code here
        res = []
        if not root:
            return []
        queue = collections.deque([root])
        
        while queue:
            level_head_dummy = ListNode(None)
            curr = level_head_dummy
            for _ in range(len(queue)):
                top = queue.popleft()
                curr.next = ListNode(top.val)
                curr = curr.next
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)
            res.append(level_head_dummy.next)
        return res