"""
374. Spiral Matrix
https://www.lintcode.com/problem/spiral-matrix/description?_from=ladder&&fromId=131
BFS
"""

DIRECTIONS = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]
from collections import deque
class Solution:
    """
    @param matrix: a matrix of m x n elements
    @return: an integer list
    """
    def spiralOrder(self, matrix):
        # write your code here
        if not matrix or not matrix[0]:
            return []
        res = []
        visited = set()
        q = deque()
        q.append((0,0,0))
        visited.add((0, 0))
        while q:
            f_d_i, f_c_x, f_c_y = q.popleft()
            res.append(matrix[f_c_x][f_c_y])
            for i in range(4):
                delta_x, delta_y = DIRECTIONS[(f_d_i + i) % 4]
                nx, ny = f_c_x + delta_x, f_c_y + delta_y
                if self.is_valid(nx, ny, matrix, visited):
                    visited.add((nx, ny))
                    q.append(((f_d_i + i) % 4, nx, ny))
                    break
        return res
                
    def is_valid(self, x, y, matrix, visited):
        n = len(matrix)
        m = len(matrix[0])
        
        if not (0 <= x < n and 0 <= y < m):
            return False
        if (x, y) in visited:
            return False
        return True