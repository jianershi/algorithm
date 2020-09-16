"""
1179.py
take 2
union find

"""
class UnionFind:
    def __init__(self):
        self.fathers = {}
        self.count = 0

    def add(self, n):
        for i in range(n):
            self.fathers[i] = i
            self.count += 1

    def find(self, x):
        if self.fathers[x] != x:
            self.fathers[x] = self.find(self.fathers[x])
        return self.fathers[x]

    def union(self, a, b):
        af = self.find(a)
        bf = self.find(b)

        if af == bf:
            return

        self.fathers[af] =  bf
        self.count -= 1
    

class Solution:
    """
    @param M: a matrix
    @return: the total number of friend circles among all the students
    """
    def findCircleNum(self, M):
        # Write your code here
        if not M:
            return 0

        n = len(M)

        uf = UnionFind()
        uf.add(n)
        for id in range(n):
            for neighbor_id, is_neighbor in enumerate(M[id]):
                if not is_neighbor:
                    continue
                uf.union(id, neighbor_id)
        return uf.count
