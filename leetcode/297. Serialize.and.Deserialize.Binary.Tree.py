"""
297. Serialize and Deserialize Binary Tree
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
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
            return json.dumps(ret)
        
        queue = collections.deque([(root)])
        
        while queue:
            level = []
            for _ in range(len(queue)):
                top = queue.popleft()
                level.append(top.val if top else None)
                if top:
                    queue.append(top.left if top.left else None)
                    queue.append(top.right if top.right else None)
            ret.append(level)
        
        return json.dumps(ret)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = json.loads(data)
        if not data:
            return None
        data = collections.deque(data)
        
        root = TreeNode(data.popleft()[0])
        queue = collections.deque([(root)])
        
        while queue:
            cur_level = deque(data.popleft())
            for _ in range(len(queue)):
                top = queue.popleft()
                cur_node_left = cur_level.popleft()
                if cur_node_left != None:
                    top.left = TreeNode(cur_node_left)
                    queue.append(top.left)
                cur_node_right = cur_level.popleft()
                if cur_node_right != None:
                    top.right = TreeNode(cur_node_right)
                    queue.append(top.right)
        
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))