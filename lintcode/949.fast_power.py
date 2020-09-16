"""
快速幂非递归写法
"""
class Solution:
    """
    @param n: an integer
    @return: return an int
    """
    def lastFourDigitsOfFn(self, n):
        # write your code here
        if n == 0:
            return 0
        if n == 1:
            return 1
        base_matrix = [[1, 1],[1, 0]]
        # result_matrix = [[1, 0], [0, 1]] #unit matrix
        power = n - 1
        while power > 0: #快速幂非递归写法，参见lintcode note. fast power lintcode 140
            if power % 2 == 1:
                result_matrix = self.matrix_multiply(result_matrix, base_matrix)
            base_matrix = self.matrix_multiply(base_matrix, base_matrix)
            power = power // 2
        return result_matrix[0][0]

    """
    比较通用的 2个matrix乘法:
    https://www.mathsisfun.com/algebra/matrix-multiplying.html
    @param: matrix1, matrix2
    @return: result matrix, or -1 if not possible to multiply to matrix
    """
    def matrix_multiply(self, matrix1, matrix2):
        m = len(matrix1) #matrix 1 m * n
        n = len(matrix1[0]) #matrix 2 n * p
        if len(matrix2) != n:
            return -1
        p = len(matrix2[0]) #result matrix m * p
        result = [[0] * p for _ in range(m)]
        for i in range(m):
            for j in range(p):
                sum = 0
                for c in range(n):
                    sum += matrix1[i][c] * matrix2[j][c]
                result[i][j] = sum % 10000

        return result


s = Solution()
print(s.lastFourDigitsOfFn(5531354))
