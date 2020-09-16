"""
405. Submatrix Sum
https://www.lintcode.com/problem/submatrix-sum/description
九章强化班C7


naive way:
using prefix sum on matrix
sum of area(x1, y1 -> x2, y2) = 
s(x2, y2) - s(x2, y1 - 1) - s(x1 - 1, y2) + s(x1 - 1, y1 - 1)
traverse both top left corner and bottom right, assume n * m matrix
time complexity
O(n * m * n * m * 1) = O(n^2 * m^2)

better way: 2D->1D
traverse starting upper bound row and lower bound row. 
define a matrix must have it's top at the upper bound and bottom at lower bound.
calculate prefix sum from left to right in this submatrix. and record 0.
time complexity
O(n * n * m)


"""
class Solution:
    """
    @param: matrix: an integer matrix
    @return: the coordinate of the left-up and right-down number
    """
    def submatrixSum(self, matrix):
        # write your code here
        if not matrix or not matrix[0]:
            return []

        n = len(matrix)
        m = len(matrix[0])

        for up in range(n):
            col_sum = [0] * (m)
            for down in range(up, n):
                prefix_sum = {0: -1} #prefix_sum[i] including i
                now_sum = 0
                for j in range(m):
                    col_sum[j] += matrix[down][j]
                    now_sum += col_sum[j]
                    if now_sum in prefix_sum:
                        return [[up, prefix_sum[now_sum] + 1],[down, j]]
                    prefix_sum[now_sum] = j
        return []
