"""
297. Serialize and Deserialize Binary Tree
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

using custom format of 
['1', '2', '3', '#', '#', '4', '5', '#', '#', '#', '#']
removing trailing #

but the code is more cumbersome to read..

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import json
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ret = []
        if not root:
            return '{}'
        
        queue = collections.deque([(root)])
        while queue:
            top = queue.popleft()
            ret.append(str(top.val) if top else "#")
            if top:
                queue.append(top.left)
                queue.append(top.right)
        
        #strip all # in the end
        j = len(ret) - 1
        while j >= 0 and ret[j] == '#':
            j -= 1
        
        return "{{{}}}".format(",".join(ret[:j + 1]))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '{}':
            return None
        data = data[1: -1]
        data = deque(data.split(","))

        root = TreeNode(data.popleft())
        queue = collections.deque([(root)])
        
        while queue:
            for _ in range(len(queue)):
                top = queue.popleft()
                #data empty because i removed all the trailing #
                if not data:
                    break
                cur_node_left = data.popleft()
                if cur_node_left != '#':
                    top.left = TreeNode(cur_node_left)
                    queue.append(top.left)
                #data empty because i removed all the trailing #
                if not data:
                    break
                cur_node_right = data.popleft()
                if cur_node_right != '#':
                    top.right = TreeNode(cur_node_right)
                    queue.append(top.right)
        
        return root
