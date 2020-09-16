"""
591. Connecting Graph III
https://www.lintcode.com/problem/connecting-graph-iii/
"""
class ConnectingGraph3:
    """
    @param a: An integer
    @param b: An integer
    @return: nothing
    """
    def __init__(self, n):
        # initialize your data structure here.
        self.father = {}
        self.count = 0
        for i in range(1, n + 1):
            self.father[i] = i
            self.count += 1

    def connect(self, a, b):
        # write your code here
        a_father = self.find(a)
        b_father = self.find(b)

        if a_father == b_father:
            return

        self.father[a_father] = b_father
        self.count -= 1


    def find(self, x):
        j = x
        while self.father[j] != j:
            j = self.father[j]

        while x != j:
            xf = self.father[x]
            self.father[x] = j
            x = xf

        return j
    """
    @return: An integer
    """
    def query(self):
        # write your code here
        return self.count
