"""
598. Zombie in Matrix
multi-starting point BFS.
change matrix to 1 as it goes
reference: https://www.jiuzhang.com/solution/zombie-in-matrix/#tag-other-lang-python
"""
from collections import deque
class Category:
    ZOMBIE = 1
    HUMAN = 0
    WALL = 2

class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """
    def zombie(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return -1

        m = len(grid)
        n = len(grid[0])

        queue = deque()
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == Category.ZOMBIE:
                    queue.append((i, j))
                    visited.add((i, j))

        steps = self.bfs(grid, queue, visited)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == Category.HUMAN:
                    return -1

        return steps

    def bfs(self, grid, queue, visited):
        DIRECTIONS = [
            (0, 1),
            (0, -1),
            (-1, 0),
            (1, 0)
        ]

        steps = -1

        while queue:
            steps += 1
            for _ in range(len(queue)):
                head = queue.popleft()
                for direction in DIRECTIONS:
                    x = head[0] + direction[0]
                    y = head[1] + direction[1]
                    if self.is_valid(grid, x, y, visited):
                        grid[x][y] = Category.ZOMBIE
                        queue.append((x, y))
                        visited.add((x, y))

        return steps

    def is_valid(self, grid, x, y, visited):
        m = len(grid)
        n = len(grid[0])

        if (x, y) in visited:
            return False
        if not (0 <= x < m and 0 <= y < n):
            return False
        if grid[x][y] == Category.ZOMBIE or grid[x][y] == Category.WALL:
            return False
        return True
