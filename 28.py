"""
28. Search a 2D Matrix
https://www.lintcode.com/problem/search-a-2d-matrix/description
"""
class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix or not matrix[0]:
            return False

        n = len(matrix)
        m = len(matrix[0])

        start, end = 0, n * m - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if self.get(matrix, mid) < target:
                start = mid
            else:
                end = mid

        if self.get(matrix, start) == target:
            return True
        if self.get(matrix, end) == target:
            return True
        return False

    def get(self, matrix, location):
        m = len(matrix[0])

        x = location // m
        y = location % m

        return matrix[x][y]
