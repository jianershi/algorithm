"""
178. Graph Valid Tree
https://www.lintcode.com/problem/graph-valid-tree/description
"""
class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here
        if len(edges) != n - 1:
            return False
        if n == 1 and edges == []:
            return True

        self.father = {}
        self.count = 0
        for a, b in edges:
            if a not in self.father:
                self.father[a] = a
                self.count += 1
            if b not in self.father:
                self.father[b] = b
                self.count += 1
            if self.union(a, b):
                self.count -= 1
        return self.count == 1

    def union(self, a, b):
        a_father = self.find(a)
        b_father = self.find(b)

        if a_father == b_father:
            return False

        self.father[a_father] = b_father
        return True

    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]
