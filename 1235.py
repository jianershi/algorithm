"""
1235. Serialize and Deserialize BST
https://www.lintcode.com/problem/serialize-and-deserialize-bst/description
"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    def serialize(self, root):
        if not root:
            return "{}"

        queue = [root]
        index = 0
        while index < len(queue):
            if queue[index] is not None:
                head = queue[index]
                queue.append(head.left)
                queue.append(head.right)
            index += 1

        while queue[-1] == None:
            queue.pop()

        return "{%s}" % ",".join(
                [
                    str(x.val)
                    if x is not None else "#"
                    for x in queue
                ]
            )

    def deserialize(self, data):
        if data == "{}":
            return None

        vals = data[1:-1].split(',')

        while vals[-1] == "#":
            vals.pop()

        root = TreeNode(int(vals[0]))
        queue = [root] #queue means TreeNode that are waiting for their left and right node to be attached

        index = 0
        
        is_left_node = True

        for val in vals[1:]:
            if val != "#":
                curr_node = TreeNode(int(val))
                if is_left_node:
                    queue[index].left = curr_node
                else:
                    queue[index].right = curr_node

                queue.append(curr_node)

            if not is_left_node:
                index += 1

            is_left_node = not is_left_node

        return root

