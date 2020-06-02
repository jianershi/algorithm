"""
654. Sparse Matrix Multiplication
refer to lecture note 高频c3
"""
class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """
    def multiply(self, A, B):
        # write your code here
        if not A or not B:
            return -1

        m = len(A)
        n = len(A[0])
        p = len(B[0])

        row_vector = [
            [
                (j, A[i][j])
                for j in range(n)
                if A[i][j] != 0
            ]
            for i in range(m)
        ]

        col_vector = [
            [
                (i, B[i][j])
                for i in range(n)
                if B[i][j] != 0
            ]
            for j in range(p)
        ]

        result = [
            [
                self.multi(row, col)
                for col in col_vector
            ]
            for row in row_vector
        ]

        return result

    def multi(self, row, col):
        i = j = 0
        sum = 0
        while i < len(row) and j < len(col):
            index_row, val_row = row[i]
            index_col, val_col = col[j]
            if index_row < index_col:
                i += 1
            elif index_row > index_col:
                j += 1
            else:
                sum += val_row * val_col
                i += 1
                j += 1
        return sum
