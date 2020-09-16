"""
1469. Longest Path On The Tree
https://www.lintcode.com/problem/longest-path-on-the-tree/description?_from=ladder&&fromId=160
maximum recursion depth exceeded
反例:
5
[0,2,2,2]
[1,0,3,4]
[1,2,5,6]
因为2个数组给的时候就没告诉是从上到下的还是从下到上的。所以把邻居光放上面的话，万一ends是根的话，
要是邻居表里面没有starts的点不就过不去了。所以真的是无向图。
"""
import heapq, sys

class MyTreeNode:
    def __init__(self, value):
        self.value = value
        self.children = {} #MyTreeNode: weight

class Tree:
    def __init__(self, starts, ends, lens):
        self.root = self.build_tree(starts, ends, lens)

    def build_tree(self, starts, ends, lens):
        map = {}
        for i in range(len(starts)):
            map[starts[i]] = map.get(starts[i], MyTreeNode(starts[i]))
        for i in range(len(ends)):
            map[ends[i]] = map.get(ends[i], MyTreeNode(ends[i]))
        for i in range(len(lens)):
            map[starts[i]].children[map[ends[i]]] = lens[i]
        return map[starts[0]]

class Solution:
    """
    @param n: The number of nodes
    @param starts: One point of the edge
    @param ends: Another point of the edge
    @param lens: The length of the edge
    @return: Return the length of longest path on the tree.
    """
    def longestPath(self, n, starts, ends, lens):
        tree = Tree(starts, ends, lens)
        memo = {}
        l_p, l_c = self.longest_path_dfs(tree.root, memo)
        return max(l_p, l_c)

    def longest_path_dfs(self, root, memo):
        if root in memo:
            return memo[root]
        if not root.children:
            memo[root] = (0, 0)
            return 0,0

        l_c = []
        l_p = -sys.maxsize
        for child in root.children:
            child_l_c, child_l_p = self.longest_path_dfs(child, memo)
            l_p = max(l_p, child_l_p)
            heapq.heappush(l_c, child_l_c + root.children[child])
            if len(l_c) > 2:
                heapq.heappop(l_c)
        l_p = max(l_p, sum(l_c))
        # print (l_c, l_p)
        memo[root] = max(l_c), l_p
        return max(l_c), l_p
