"""
590. Connecting Graph II
https://www.lintcode.com/problem/connecting-graph-ii/description
"""
class ConnectingGraph2:
    """
    @param: n: An integer
    """
    def __init__(self, n):
        # do intialization if necessary
        self.fathers = {}
        self.size = {}
        for i in range(1, n + 1):
            self.fathers[i] = i
            self.size[i] = 1

    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """
    def connect(self, a, b):
        # write your code here
        a_father = self.find(a)
        b_father = self.find(b)
        if a_father == b_father:
            return

        self.fathers[a_father] = b_father
        self.size[b_father] += self.size[a_father]

    def find(self, x):
        if self.fathers[x] == x:
            return x
        self.fathers[x] = self.find(self.fathers[x])
        return self.fathers[x]
    """
    @param: a: An integer
    @return: An integer
    """
    def query(self, a):
        # write your code here
        return self.size[self.find(a)]
