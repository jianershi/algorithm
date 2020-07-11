"""
291. Second Diameter
https://www.lintcode.com/problem/second-diameter/description?_from=contest&&fromId=95
"""
from collections import deque
class Solution:
    """
    @param edge: edge[i][0] [1] [2]  start point,end point,value
    @return: return the second diameter length of the tree
    """
    def getSecondDiameter(self, edge):
        # write your code here
        n = len(edge)
        graph = {} #{node: {node:distance}}
        for e in edge:
            if e[0] not in graph:
                graph[e[0]] = {}
            graph[e[0]][e[1]] = e[2]
            if e[1] not in graph:
                graph[e[1]] = {}
            graph[e[1]][e[0]] = e[2]


        longest_index, _ = self.bfs(edge[0][0], graph)
        longest_index, distance1 = self.bfs(longest_index, graph)
        _, distance2 = self.bfs(longest_index, graph)

        return max(sorted(distance1.values())[-2],sorted(distance2.values())[-2])

    def bfs(self, root, graph):
        queue = deque([(root, 0)])
        distance = {root: 0}

        while queue:
            now, dist = queue.popleft()
            for node in graph[now]:
                if node in distance:
                    continue
                queue.append((node, dist + graph[now][node]))
                distance[node] = dist + graph[now][node]

        max_dist = 0
        max_dist_key = None
        for key, value in distance.items():
            if value > max_dist:
                max_dist = value
                max_dist_key = key
        return max_dist_key, distance