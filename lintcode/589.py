"""
589. Connecting Graph
https://www.lintcode.com/problem/connecting-graph/description
"""
class ConnectingGraph:
    """
    @param: n: An integer
    """
    def __init__(self, n):
        # do intialization if necessary
        self.fathers = {}
        for i in range(n + 1):
            self.fathers[i] = i

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

    # def find(self, x):
    #     j = x
    #     while self.fathers[j] != j:
    #         j = self.fathers[j]

    #     while (x != j):
    #         fx = self.fathers[x]
    #         self.fathers[x] = j
    #         x = fx

    #     return j

    #recursion find
    def find(self, x):
        if self.fathers[x] == x:
            return x
        self.fathers[x] = self.find(self.fathers[x])
        return self.fathers[x]

    """
    @param: a: An integer
    @param: b: An integer
    @return: A boolean
    """
    def query(self, a, b):
        # write your code here
        return self.find(a) == self.find(b)
