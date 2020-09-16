"""
629. Minimum Spanning Tree
https://www.lintcode.com/problem/minimum-spanning-tree/description
original auther 明尼苏达大角羊 from
https://www.jiuzhang.com/solution/minimum-spanning-tree/#tag-other

optimized using
Weighted Quick-Union with Path Compression
https://blog.csdn.net/dm_vincent/article/details/7655764
amortized O(1) for union and find operation
"""
'''
Definition for a Connection
class Connection:

    def __init__(self, city1, city2, cost):
        self.city1, self.city2, self.cost = city1, city2, cost
'''
class Solution:
    # @param {Connection[]} connections given a list of connections
    # include two cities and cost
    # @return {Connection[]} a list of connections from results
    def __init__(self):
        self.father = {}
        self.uf_count = 0

    def lowestCost(self, connections):
        # Write your code here
        connections.sort(key=lambda x: (x.cost, x.city1, x.city2))

        result = []

        self.uf(connections)
        print(self.father)
        self.union_all(connections, result)

        if self.uf_count == 1:
            return result
        return []


    def uf(self, connections):
        for connection in connections:
            for city in (connection.city1, connection.city2):
                if city not in self.father:
                    self.father[city] = city
                    self.uf_count += 1

    def union_all(self, connections, result):
        for connection in connections:
            success = self.union(connection.city1, connection.city2)
            if success:
                result.append(connection)

    def union(self, a, b):
        a_father = self.find(a)
        b_father = self.find(b)

        if a_father == b_father:
            return False

        self.father[a_father] = b_father
        self.uf_count -= 1

        return True

    def find(self, city):
        if self.father[city] == city:
            return city
        self.father[city] = self.find(self.father[city])
        return self.father[city]
