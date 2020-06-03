"""
1840. Matrix restoration
"""
class Solution:
    """
    @param n: the row of the matrix
    @param m: the column of the matrix
    @param after: the matrix
    @return: restore the matrix
    """
    def matrixRestoration(self, n, m, after):
        # write your code here
        if not after or not after[0]:
            return after

        before_matrix = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                before_matrix[i][j] = after[i][j]
                if j > 0:
                    before_matrix[i][j] -= after[i][j - 1]
                if i > 0:
                    before_matrix[i][j] -= after[i - 1][j]
                if i > 0 and j > 0:
                    before_matrix[i][j] += after[i - 1][j - 1]

        return before_matrix
