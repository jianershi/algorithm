"""
133. Clone Graph
https://leetcode.com/problems/clone-graph/

general idea
bfs search with visited sets

"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        queue = deque([node])
        root = Node(node.val)
        res = {node: root} #served as visited sets {existing node: new node}
        
        while queue:
            top = queue.popleft()
            for neighbor in top.neighbors:
                if neighbor not in res:
                    node = Node(neighbor.val)
                    queue.append(neighbor)
                    res[neighbor] = node
                else:
                    node = res[neighbor]

                if node not in res[top].neighbors:
                    res[top].neighbors.append(node)
        
        return root
            