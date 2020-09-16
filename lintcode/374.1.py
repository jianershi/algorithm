"""
374. Spiral Matrix
https://www.lintcode.com/problem/spiral-matrix/description?_from=ladder&&fromId=131
DFS
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
        self.dfs(matrix, 0, 0, 0, set([(0, 0)]), res)
        return res
                
    def dfs(self, matrix, x, y, d, v, res):
        res.append(matrix[x][y])
        
        for i in range(4):
            delta_x, delta_y = DIRECTIONS[(d + i) % 4]
            nx, ny = x + delta_x, y + delta_y
            if not self.is_valid(nx, ny, matrix, v):
                continue
            v.add((nx, ny))
            self.dfs(matrix, nx, ny, (d + i) % 4, v, res)
            v.pop()
            break
            
    def is_valid(self, x, y, matrix, visited):
        n = len(matrix)
        m = len(matrix[0])
        
        if not (0 <= x < n and 0 <= y < m):
            return False
        if (x, y) in visited:
            return False
        return True