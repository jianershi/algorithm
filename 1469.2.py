"""
1469. Longest Path On The Tree
https://www.lintcode.com/problem/longest-path-on-the-tree/description?_from=ladder&&fromId=160
maximum recursion depth exceeded
using DFS to build undirectional graph instead of tree
九章高频课dfs写法
"""
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

        visited = set()
        visited.add(0)

        max_path, max_chain = self.dfs(0, visited, neighbors) #可以放入任意开始位置
        return max_path

    def dfs(self, root, visited, neighbors):
        #没有出口，因为是图，等neighbor里东西没了就结束了
        max_path, max_chain = 0, 0

        max_chain_child, second_max_chain_child = 0, 0

        for neighbor, distance in neighbors[root]:
            if neighbor in visited:
                continue
            visited.add(neighbor)
            child_path, child_chain = self.dfs(neighbor, visited, neighbors)
            child_chain += distance
            visited.remove(neighbor)

            max_path = max(max_path, child_path)
            max_chain = max(max_chain, child_chain)

            _, second_max_chain_child, max_chain_child = sorted([max_chain_child, second_max_chain_child, child_chain])

        max_path = max(max_path, max_chain_child + second_max_chain_child)
        return max_path, max_chain
