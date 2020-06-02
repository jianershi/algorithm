"""
946. 233 Matrix
reference: https://zhuanlan.zhihu.com/p/42639682
my note: https://imgur.com/a/WtcwXXK
"""
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

        transformation_matrix = self.build_transformation_matrix(len(X))

        #last column = = transformation ^ x * first_column
        answer = self.multiply_matrix(self.fast_power(transformation_matrix, m, mod), self.build_first_column(X), mod)

        # answer at last column[n]
        # return answer[len(X)] % mod
        return answer[len(X)][0] % mod

    def fast_power(self, matrix, power, mod):
        answer = self.build_identity_matrix(len(matrix))
        while power > 0:
            if power & 1 == 1:
                answer = self.multiply_matrix(answer, matrix, mod)
            matrix = self.multiply_matrix(matrix, matrix, mod)
            power >>= 1
        return answer
    """
    multiplying 2 matrix
    @param: matrix1, matrix2
    @returns: resulting matrix % mod, return -1 if unable
    """
    def multiply_matrix(self, matrix1, matrix2, mod):
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
                    sum += matrix1[i][k] * matrix2[k][j] % mod
                result[i][j] = sum
        return result

    """
    Build transformation matrix.
    If the X is of size n, the matrix is of size (n + 2) * (n + 2)
    @param: n, size of X
    @return: a tranformation matrix
    """
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

    """
    build first column
    @param: X
    @return: a matrix consists of first column.
            It is built of size len(X) + 2,
            with first element = 23 and last element = 3
            and middle elements from X
    """
    def build_first_column(self, X):
        matrix = [[0] for _ in range(len(X) + 2)]
        matrix[0][0] = 23
        matrix[len(X) + 1][0] = 3
        for i in range(1, len(X) + 1):
            matrix[i][0] = X[i - 1]

        return matrix

    def build_identity_matrix(self, k):
        matrix = [[0] * k for _ in range(k)]
        for i in range(k):
            matrix[i][i] = 1
        return matrix

s = Solution()
X=[]
m=100
result = s.calcTheValueOfAnm(X, m)
# for i in result:
    # print(i)
print (result)
