"""
133. Clone Graph
https://leetcode.com/problems/clone-graph/

general idea
bfs search with visited sets

the res = visited sets, using original nodes as key and newly created nodes as value
1. if neighbor of a node is not visited:
    1. deep copy that node and update visited sets
    2. put original node into the queue
    3. update current node(copied)'s neighbors
        * since this is the first time and only time we are processing this node in this queue, meaning this node's neighbor's were never written. 
        1) for newly created neighbours, of course those neighbors were never in current node's neighbor list
        2) for neighbors already visited, such as 4->1, since we are processing node 4, node 4 itself was created when node 1 is populated, but node's 4's neighbor list was only written when it's node's 4th turn to scan it's neighbors. so node 4's neighbor list was never written.

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
        res = {}#served as visited sets {existing node: new node}
        res[node] =  Node(node.val)
        
        while queue:
            top = queue.popleft()
            for neighbor in top.neighbors:
                if neighbor not in res:
                    res[neighbor] = Node(neighbor.val) #if neighbor not visited, copy and put in res
                    queue.append(neighbor)
                    
                res[top].neighbors.append(res[neighbor]) #update current node's neighbor list
        
        return res[node]