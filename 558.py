"""
558. Sliding Window Matrix Maximum
https://www.lintcode.com/problem/sliding-window-matrix-maximum/description?_from=ladder&&fromId=106

2d prefix sum
"""
class Solution:
    """
    @param matrix: an integer array of n * m matrix
    @param k: An integer
    @return: the maximum number
    """
    def maxSlidingMatrix(self, matrix, k):
        # write your code here
        if not matrix or not matrix[0]:
            return 0

        n = len(matrix)
        m = len(matrix[0])

        if n < k or m < k:
            return 0

        prefix_sum = self.build_prefix_sum(matrix)

        max_sum = -sys.maxsize
        for i in range(k, n + 1):
            for j in range(k, m + 1):
                partial_sum = prefix_sum[i][j] - prefix_sum[i - k][j] - prefix_sum[i][j - k] + prefix_sum[i - k][j - k]
                max_sum = max(max_sum, partial_sum)
        return max_sum

    def build_prefix_sum(self, matrix):
        n = len(matrix)
        m = len(matrix[0])

        prefix_sum = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                prefix_sum[i][j] = prefix_sum[i - 1][j]     \
                                + prefix_sum[i][j - 1]      \
                                - prefix_sum[i - 1][j - 1]  \
                                + matrix[i - 1][j - 1]
        return prefix_sum