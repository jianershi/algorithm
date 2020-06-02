"""
629. Minimum Spanning Tree
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
    def lowestCost(self, connections):
        # Write your code here
        connections.sort(key=lambda x: (x.cost, x.city1, x.city2))

        father = {}
        father_size = {}
        count = 0

        result = []

        count = self.uf(father, father_size, count, connections)
        count = self.union_all(father, father_size, count, connections, result)

        if count == 1:
            return result
        return []

    def uf(self, father, father_size, count, connections):
        for connection in connections:
            for city in (connection.city1, connection.city2):
                if city not in father:
                    father[city] = city
                    father_size[city] = 1
                    count += 1
        return count

    def union_all(self, father, father_size, count, connections, result):
        for connection in connections:
            count, success = self.union(father, father_size, count, connection.city1, connection.city2)
            if success:
                result.append(connection)

        return count

    def union(self, father, father_size, count, a, b):
        a_father = self.find(a, father)
        b_father = self.find(b, father)

        if a_father == b_father:
            return count, False

        if father_size[a_father] < father_size[b_father]:
            father[a_father] = b_father
            father_size[b_father] += father_size[a_father]
        else:
            father[b_father] = a_father
            father_size[a_father] += father_size[b_father]

        return count - 1, True

    def find(self, city, father):
        while father[city] != city:
            father[city] = father[father[city]] #compression
            city = father[city]

        return city
