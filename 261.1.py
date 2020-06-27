"""
261. Maximum Connected Area
https://www.lintcode.com/problem/maximum-connected-area/description?_from=contest&&fromId=

thought:
traverse all starting point with 1, but record each area's area.
then traverse all 0, to see how many *diffrernt* area connected, add all areas up


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
        areas = {} #starting point, area
        visited = {} #position, starting position
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1 and (i, j) not in visited:
                    visited[(i, j)] = (i, j)
                    areas[(i,j)] = self.bfs(i, j, matrix, visited)

        for i in range(n):
            for j in range(m):
                if matrix[i][j] != 0:
                    continue
                all_area_black = False
                connected_area = 0
                connected_components = set()
                for delta in DIRECTIONS:
                    n_x, n_y = i + delta[0], j + delta[1]
                    if not (0 <= n_x < n and 0 <= n_y < m):
                        continue
                    if (n_x, n_y) in visited and visited[(n_x ,n_y)] not in connected_components:
                       connected_area += areas[visited[(n_x, n_y)]]
                       connected_components.add(visited[(n_x, n_y)])

                max_area = max(max_area, connected_area + 1)

        return max_area if not all_area_black else n * m

    def bfs(self, start_x, start_y, matrix, visited):
        queue = deque([(start_x, start_y)])

        count = 1
        while queue:
            x, y = queue.popleft()
            for delta in DIRECTIONS:
                n_x, n_y = x + delta[0], y + delta[1]
                if not self.is_valid(n_x, n_y, matrix, visited):
                    continue
                queue.append((n_x, n_y))
                visited[(n_x, n_y)] = (start_x, start_y)
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