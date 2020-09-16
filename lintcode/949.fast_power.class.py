"""
快速幂非递归写法
用class类包装了 Matrix
"""
import sys
class Matrix:
    def __init__(self, m, n, mod=sys.maxsize, unit_matrix=False): #create m * n matrix
        self.m = m
        self.n = n
        self.mod = mod
        self.mat = [[0] * n for _ in range(m)]
        if unit_matrix:
            self.set_unit_matrix()

    def __mul__(self, matrix):
        result = Matrix(self.m, matrix.n)
        result.mod = self.mod
        if matrix.m != self.n:
            return -1
        p = matrix.n

        for i in range(self.m):
            for j in range(matrix.n):
                for k in range(self.n):
                    result.mat[i][j] += ((self.mat[i][k] % self.mod) * (matrix.mat[k][j] % self.mod)) % self.mod
                result.mat[i][j] %= self.mod
        return result

    def set_unit_matrix(self): #m * m unit matrix
        for i in range(self.m):
            self.mat[i][i] = 1

class Solution:
    """
    @param n: an integer
    @return: return an int
    """
    def lastFourDigitsOfFn(self, n):
        MOD = 10000
        # write your code here
        if n == 0:
            return 0
        if n == 1:
            return 1

        base_matrix = Matrix(2, 2, MOD)
        base_matrix.mat = [[1, 1],[1, 0]]
        result_matrix = Matrix(2,2, MOD, unit_matrix=True)

        power = n - 1
        while power > 0: #快速幂非递归写法，参见lintcode note. fast power lintcode 140
            if power & 1:
                result_matrix = result_matrix * base_matrix
            base_matrix = base_matrix * base_matrix
            power >>= 1

        return result_matrix.mat[0][0]


s = Solution()
print(s.lastFourDigitsOfFn(5531354))
