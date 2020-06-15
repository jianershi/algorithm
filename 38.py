"""
38. Search a 2D Matrix II
https://www.lintcode.com/problem/search-a-2d-matrix-ii/description
"""
class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix)
        m = len(matrix[0])

        match = 0

        i, j = n - 1, 0
        while i >=0 and j < m:
            if matrix[i][j] < target:
                j += 1
            elif matrix[i][j] > target:
                i -= 1
            else:
                match += 1
                j += 1
                i -= 1

        return match
