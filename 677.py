"""
677. Number of Big Islands
for anything start with 1, BFS search all connected 1.
until queue is empty -> the size of current island

traver to the next none 0 point. and do BFS again

"""
from collections import deque
class Solution:
    """
    @param grid: a 2d boolean array
    @param k: an integer
    @return: the number of Islands
    """
    def numsofIsland(self, grid, k):
        # Write your code here
        if not grid or not grid[0]:
            return 0

        m = len(grid)
        n = len(grid[0])

        count = 0
        visited = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    count += self.bfs(grid, i, j, k, visited)

        return count

    """

    """
    def bfs(self, grid, start_i, start_j, k, visited):
        DIRECTIONS = [
            (0, 1),
            (0, -1),
            (-1, 0),
            (1, 0)
        ]

        queue = deque([(start_i, start_j)])
        visited.add((start_i, start_j))

        count = 0
        while queue:
            head = queue.popleft()
            count += 1
            for direction in DIRECTIONS:
                x = head[0] + direction[0]
                y = head[1] + direction[1]
                if self.is_valid(grid, x, y, visited):
                    queue.append((x, y))
                    visited.add((x, y))

        return 1 if count >= k else 0

    """
    check is 1 and inside the grid and not previously visited and are 1
    @param: grid, x, y, visited
    @return True if valid entry False if not
    """
    def is_valid(self, grid, x, y, visited):
        if (x, y) in visited:
            return False

        m = len(grid)
        n = len(grid[0])

        if not (0 <= x < m and 0 <= y < n):
            return False

        if grid[x][y] != 1:
            return False

        return True
