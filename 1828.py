"""
1828. Lake Escape
https://www.lintcode.com/problem/lake-escape/description
  0  1  2  3  4  5  6
0[0, 0, 0, 0, 0, 0, 0]
1[0, 0,-1, 0, 0, 0, 0]
2[0, 0, 1,-1, 0,-1, 0]
3[-1,0, 1, 0, 0, 0, 0]
4[0, 1, 1, 0, 0, 1, 0]
5[-1,0,-1, 0,-1, 0, 0]
6[0, 0, 0, 0, 0, 0, 0]

"""
from collections import deque
class DataType:
    ICE = 0
    SNOWBANK = 1
    HOLE = -1

DIRECTIONS = [
    (0, 1),
    (0, -1),
    (-1, 0),
    (1, 0)
]

class Solution:
    """
    @param side_length: the length of a side of the lake (it's a square)
    @param lake_grid: a 2D matrix representing the lake 0= ice, 1= snowbank, -1= hole
    @param albert_row: row of Albert's snowbank
    @param albert_column: column of Albert's snowbank
    @param kuna_row: row of Kuna's snowbank
    @param kuna_column: column of Kuna's snowbank
    @return: a bool - whether Albert can escape
    """

    def lakeEscape(self, side_length, lake_grid, albert_row, albert_column, kuna_row, kuna_column):
        # write your code here
        queue = deque([(albert_row, albert_column)])
        dog = (kuna_row, kuna_column)
        visited = set([(albert_row, albert_column)])
        dog_saved = False
        can_escape = False
        while queue:
            x, y = queue.popleft()
            if (x, y) == dog:
                dog_saved = True
            for delta in DIRECTIONS:
                next_x, next_y = self.safe_destination(lake_grid, x, y, visited, delta)
                if (next_x, next_y) == (-1, -1):
                    continue
                if lake_grid[next_x][next_y] == DataType.SNOWBANK:
                    queue.append((next_x, next_y))
                if self.can_escape(lake_grid, next_x, next_y):
                    can_escape = True
                visited.add((next_x, next_y))

        return dog_saved and can_escape

    def safe_destination(self, lake_grid, x, y, visited, delta):
        n = len(lake_grid)
        m = len(lake_grid[0])
        next_x, next_y = x, y
        while 0 <= next_x + delta[0] < n and 0 <= next_y + delta[1] < m:
            next_x += delta[0]
            next_y += delta[1]
            if lake_grid[next_x][next_y] == DataType.SNOWBANK:
                break
            if lake_grid[next_x][next_y] == DataType.HOLE:
                return -1, -1
        if (next_x, next_y) in visited:
            return -1, -1
        return (next_x, next_y)

    def can_escape(self, lake_grid, next_x, next_y):
        n = len(lake_grid)
        m = len(lake_grid[0])
        if lake_grid[next_x][next_y] == DataType.ICE:
            return True
        if lake_grid[next_x][next_y] == DataType.SNOWBANK:
            if next_x == 0 or next_x == n - 1 or next_y == 0 or next_y == m - 1:
                return True

        return False


s = Solution()
side_length = 7
lake_grid = [[0,0,0,0,0,0,0],[0,0,-1,0,0,0,0],[0,0,1,-1,0,-1,0],[-1,0,1,0,0,0,0],[0,1,1,0,0,1,0],[-1,0,-1,0,-1,0,0],[0,0,0,0,0,0,0]]
albert_row = 4
albert_column = 1
kuna_row = 3
kuna_column = 2
print(s.lakeEscape(side_length, lake_grid, albert_row, albert_column, kuna_row, kuna_column))
