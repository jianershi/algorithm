"""
785. Is Graph Bipartite?
https://leetcode.com/problems/is-graph-bipartite/
dfs
"""
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [-1] * n
        
        for i in range(n):
            if colors[i] == -1:
                if not self.dfs(graph, colors, i, 0):
                    return False
        return True
    
    def dfs(self, graph, colors, node, color):
        n = len(graph)
        colors[node] = color
        for e in graph[node]:
            if colors[e] != -1 and colors[e] == color:
                return False
            elif colors[e] == -1 and not self.dfs(graph, colors, e, 1 - color):
                return False
        return True