"""
1469. Longest Path On The Tree
https://www.lintcode.com/problem/longest-path-on-the-tree/description?_from=ladder&&fromId=160

second go BFS
九章高频课2遍BFS写法。看note
"""
import collections
class Solution:
    """
    @param n: The number of nodes
    @param starts: One point of the edge
    @param ends: Another point of the edge
    @param lens: The length of the edge
    @return: Return the length of longest path on the tree.
    """
    def longestPath(self, n, starts, ends, lens):
        neighbors = {}
        for i in range(n - 1):
            start = starts[i]
            end = ends[i]
            length = lens[i]

            if start not in neighbors:
                neighbors[start] = []
            if end not in neighbors:
                neighbors[end] = []
            neighbors[start].append((end, length))
            neighbors[end].append((start, length)) #无向图，两边都连

        start, _ = self.bfs(0, neighbors)
        _, dist = self.bfs(start, neighbors)
        return dist

    def bfs(self, root, neighbors):
        queue = collections.deque([root])
        distance = {root:0}
        max_node, max_dist = None, 0
        while queue:
            now = queue.popleft()
            if distance[now] > max_dist:
                max_node = now
                max_dist = distance[now]

            for neighbor, edge_length in neighbors[now]:
                if neighbor in distance:
                    continue

                queue.append(neighbor)
                distance[neighbor] = distance[now] + edge_length

        return max_node, max_dist
