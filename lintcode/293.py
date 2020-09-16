"""
293. The depth of the tunnel
https://www.lintcode.com/problem/the-depth-of-the-tunnel/description?_from=contest&&fromId=96
"""
DIRECTIONS = [
    (0, 1),
    (0, -1),
    (-1, 0),
    (1, 0)
]
from collections import deque
class Solution:
    """
    @param matrix: the matrix in problem
    @return: the depth of the tunnel.
    """
    def FindDepth(self, matrix):
        #
        if not matrix or not matrix[0] or len(matrix) == 0:
            return 0
        n = len(matrix)
        m = len(matrix[0])
        if matrix[0][0] != 1 or matrix[0][m - 1] != 1:
            return 0
        
        q = deque([(0, 0)])
        v = set([(0, 0)])
        max_depth = 0
        while q:
            x, y = q.popleft()
            max_depth = max(max_depth, x)
            count = 1
            for delta_x, delta_y in DIRECTIONS:
                n_x, n_y = x + delta_x, y + delta_y
                if not self.is_valid(n_x, n_y, matrix, v):
                   continue
                count += 1
            if count > 2:
                continue
            for delta_x, delta_y in DIRECTIONS:
                n_x, n_y = x + delta_x, y + delta_y
                if not self.is_valid(n_x, n_y, matrix, v):
                   continue
                q.append((n_x, n_y))
                v.add((n_x, n_y))
               
        return max_depth
        
    def is_valid(self, x, y, matrix, visited):
        n = len(matrix)
        m = len(matrix[0])
        if not (0 <= x < n and 0 <= y < m):
            return False
        if (x, y) in visited:
            return False
        if matrix[x][y] != 1:
            return False
        return True

s = Solution()
matrix = [[1,0,0,0,1],[1,1,0,0,1],[0,1,0,1,1],[0,1,1,1,0],[0,0,0,0,0]]
print(s.FindDepth(matrix))