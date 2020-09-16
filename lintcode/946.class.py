"""
946. 233 Matrix
reference: https://zhuanlan.zhihu.com/p/42639682
my note: https://imgur.com/a/WtcwXXK
"""
import sys
class Matrix:
    def __init__(self, m, n, mod=sys.maxsize, identity_matrix=False): #create m * n matrix
        self.m = m
        self.n = n
        self.mod = mod
        self.mat = [[0] * n for _ in range(m)]
        if identity_matrix:
            self.set_identity_matrix()

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

    def set_identity_matrix(self): #m * m unit matrix
        for i in range(self.m):
            self.mat[i][i] = 1

class Solution:
    """
    @param X: a list of integers
    @param m: an integer
    @return: return an integer
    """
    def calcTheValueOfAnm(self, X, m):
        mod = 10000007
        if not X and m == 0:
            return 0

        transformation_matrix = self.build_transformation_matrix(len(X), mod)

        answer = self.fast_power(transformation_matrix, m, mod) * self.build_first_column(X, mod)

        return answer.mat[len(X)][0] % mod

    def fast_power(self, matrix, power, mod):
        answer = Matrix(matrix.m, matrix.m, mod=mod, identity_matrix=True)
        while power > 0:
            if power & 1:
                answer *= matrix
            matrix *= matrix
            power >>= 1
        return answer


    """
    Build transformation matrix.
    If the X is of size n, the matrix is of size (n + 2) * (n + 2)
    @param: n, size of X
    @return: a tranformation matrix
    """
    def build_transformation_matrix(self, n, mod):
        matrix = Matrix(n + 2, n + 2, mod)

        for i in range(n + 1):
            matrix.mat[i][0] = 10
        for i in range(n + 2):
            matrix.mat[i][n + 1] = 1
        for i in range(n + 1):
            for c in range(1, i + 1):
                matrix.mat[i][c] = 1

        return matrix

    """
    build first column
    @param: X
    @return: a matrix consists of first column.
            It is built of size len(X) + 2,
            with first element = 23 and last element = 3
            and middle elements from X
    """
    def build_first_column(self, X, mod):
        matrix = Matrix(len(X) + 2, 1, mod)
        matrix.mat[0][0] = 23
        matrix.mat[len(X) + 1][0] = 3
        for i in range(1, len(X) + 1):
            matrix.mat[i][0] = X[i - 1]

        return matrix

s = Solution()
X=[]
m=100
result = s.calcTheValueOfAnm(X, m)
# for i in result:
    # print(i)
print (result)
