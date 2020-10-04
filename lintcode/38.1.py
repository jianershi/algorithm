"""
38. Search a 2D Matrix II
https://www.lintcode.com/problem/search-a-2d-matrix-ii/description
右上角->左下角
"""
class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        n, m = len(matrix), len(matrix[0])
        i, j = 0, m - 1
        match = 0
        while i < n and j >= 0:
            if target < matrix[i][j]:
                j -= 1
            elif target > matrix[i][j]:
                i += 1
            else:
                match +=1
                i += 1
                j -= 1
        return match