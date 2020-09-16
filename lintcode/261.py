"""
261. Maximum Connected Area
https://www.lintcode.com/problem/maximum-connected-area/description?_from=contest&&fromId=

thought:
traverse all starting point with 0, then do bfs. count while doing bfs
special case:
when entire board is 1. then return n * m

time complexity: worst case: (O(m^2 n^2))


TLE
"""
from collections import deque
DIRECTIONS = [
    (0, 1),
    (0, -1),
    (-1, 0),
    (1, 0)
]
class Solution:
    """
    @param matrix: the matrix for calculation.
    @return: return the max area after operation at most once.
    """
    def maxArea(self, matrix):
        # write your code here.
        if not matrix or not matrix[0]:
            return 0

        n = len(matrix)
        m = len(matrix[0])

        all_area_black = True

        max_area = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    all_area_black = False
                    count = self.bfs(i, j, matrix)
                    max_area = max(max_area, count)

        return max_area if not all_area_black else n * m

    def bfs(self, start_x, start_y, matrix):
        queue = deque([(start_x, start_y)])
        visited = set([(start_x, start_y)])

        count = 1
        while queue:
            x, y = queue.popleft()
            for delta in DIRECTIONS:
                n_x, n_y = x + delta[0], y + delta[1]
                if not self.is_valid(n_x, n_y, matrix, visited):
                    continue
                queue.append((n_x, n_y))
                visited.add((n_x, n_y))
                count += 1

        return count

    def is_valid(self, x, y, matrix, visited):
        n = len(matrix)
        m = len(matrix[0])

        if not (0 <= x < n and 0 <= y < m):
            return False

        if (x, y) in visited:
            return False

        if matrix[x][y] == 0:
            return False

        return True

s = Solution()
matrix = [
[0,1,1,0,0,0],
[0,0,1,0,0,1],
[0,0,0,1,1,0],
[0,0,0,1,0,0]
]
print(s.maxArea(matrix))