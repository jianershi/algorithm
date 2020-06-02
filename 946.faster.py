"""
946. 233 Matrix
reference: https://zhuanlan.zhihu.com/p/42639682
my note: https://imgur.com/a/WtcwXXK
"""
import sys
class Solution:
    """
    @param X: a list of integers
    @param m: an integer
    @return: return an integer
    """
    def calcTheValueOfAnm(self, X, m):
        if not X and m == 0:
            return 0

        transformation_matrix = self.build_transformation_matrix(len(X))
        answer = self.build_first_column(X)

        """
        in order to calculate [transformation_matrix] ^ m * first_column
        we can save the time of builidng identity matrix by doing
        answer = first_column
        answer = transformation_matrix * first_column
        answer = transformation_matrix * answer
        .
        .
        .
        since matrix multiplication allows parenthethis, this is a bit faster.
        """
        while m > 0:
            if m & 1 == 1:
                answer = self.multiply_matrix(transformation_matrix, answer)
            transformation_matrix = self.multiply_matrix(transformation_matrix, transformation_matrix)
            m >>= 1

        return answer[len(X)][0] % 10000007

    def multiply_matrix(self, matrix1, matrix2):
        if not matrix1 or not matrix2:
            return -1 #error
        m = len(matrix1)
        n = len(matrix1[0])
        if len(matrix2) != n:
            return -1 #error
        p = len(matrix2[0])

        result = [[0] * p for _ in range(m)]

        for i in range(m):
            for j in range(p):
                sum = 0
                for k in range(n):
                    sum += matrix1[i][k] * matrix2[k][j] % 10000007
                result[i][j] = sum
        return result

    def build_transformation_matrix(self, n):
        matrix = [[0] * (n + 2) for _ in range(n + 2)]

        for i in range(n + 1):
            matrix[i][0] = 10
        for j in range(1, n + 1):
            matrix[0][j] = 0
        for j in range(1, n + 1):
            matrix[n + 1][j] = 0
        for i in range(n + 2):
            matrix[i][n + 1] = 1
        for i in range(1, n + 1):
            for c in range(1, i + 1):
                matrix[i][c] = 1

        return matrix

    def build_first_column(self, X):
        matrix = [[0] for _ in range(len(X) + 2)]
        matrix[0][0] = 23
        matrix[len(X) + 1][0] = 3
        for i in range(1, len(X) + 1):
            matrix[i][0] = X[i - 1]

        return matrix
