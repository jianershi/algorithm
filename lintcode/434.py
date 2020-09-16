"""
434. Number of Islands II
https://www.lintcode.com/problem/number-of-islands-ii/description
"""
"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
DIRECTIONS = [
    (0, 1),
    (0, -1),
    (-1, 0),
    (1, 0)
]
class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """
    def __init__(self):
        self.father = {}

    def numIslands2(self, n, m, operators):
        # write your code here
        islands = set()

        count = 0
        results = []
        for operator in operators:
            x, y = operator.x, operator.y
            if (x, y) in islands:
                results.append(count)
                continue
            self.father[(x, y)] = (x, y)
            islands.add((x, y))
            count += 1
            for delta in DIRECTIONS:
                next_x, next_y = x + delta[0], y + delta[1]
                if self.is_valid(n, m, next_x, next_y, islands):
                    if self.union((next_x, next_y), (x, y)):
                        count -= 1
            results.append(count)

        return results

    def is_valid(self, n, m, x, y, islands):
        if (x, y) not in islands:
            return False
        if not (0 <= x < n and 0 <= y < m):
            return False
        return True

    def union(self, a, b):
        father_a = self.find(a)
        father_b = self.find(b)

        if father_a == father_b:
            return False
        self.father[father_a] = father_b
        return True

    def find(self, x):
        if x == self.father[x]:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]
