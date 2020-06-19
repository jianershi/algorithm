"""
1179. Friend Circles

https://www.lintcode.com/problem/friend-circles/description

union find, with non-recursive find
"""
class UnionFind:
    def __init__(self):
        self.father = {}
        self.count = 0

    def find(self, x):
        j = x
        while self.father[j] != j:
            j = self.father[j]

        while x != j:
            xf = self.father[x]
            self.father[x] = j
            x = xf

        return j

    def union(self, a, b):
        a_father = self.find(a)
        b_father = self.find(b)

        if a_father == b_father:
            return

        self.father[a_father] = b_father
        self.count -= 1

    def add(self, x):
        if x not in self.father:
            self.father[x] = x
            self.count += 1

class Solution:
    """
    @param M: a matrix
    @return: the total number of friend circles among all the students
    """
    def findCircleNum(self, M):
        uf = UnionFind()
        for person_id, friends_list in enumerate(M):
            uf.add(person_id)
            for friend_id in range(len(friends_list)):
                if friends_list[friend_id] == 0:
                    continue
                uf.add(friend_id)
                uf.union(person_id, friend_id)

        return uf.count
