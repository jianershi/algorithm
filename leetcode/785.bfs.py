"""
785. Is Graph Bipartite?
https://leetcode.com/problems/is-graph-bipartite/
bfs
"""
from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [-1] * n
        for i in range(n):
            if colors[i] == -1 and not self.bfs(i, colors, graph):
                return False
            
        return True
            
    def bfs(self, i, colors, graph):
        q = deque([i])
        colors[i] = 0
        
        while q:
            f = q.popleft()
            for neighbor in graph[f]:
                if colors[neighbor] == colors[f]:
                    return False
                if colors[neighbor] == -1:
                    colors[neighbor] = 1 - colors[f]
                    q.append(neighbor)
        
        return True