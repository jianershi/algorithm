"""
573. Build Post Office II
You cannot pass through wall and house, but can pass through empty.
You only build post office on an empty.
"""
import sys
class Category:
    HOUSE = 1
    WALL = 2
    EMPTY = 0

class Solution:
    """
    @param grid: a 2D grid
    @return: An integer
    """
    def shortestDistance(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return -1

        n = len(grid)
        m = len(grid[0])

        """
        contents equals to a map from this house to any location's shortest distance sum
        """
        min_dist_to_point = [[0] * m for _ in range(n)] #impossible to have distance 0 from post office -> house
        able_to_reach = [[0] * m for _ in range(n)]

        house_count = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == Category.HOUSE:
                    self.bfs(i, j, grid, min_dist_to_point, able_to_reach)
                    house_count += 1

        min_total_steps = sys.maxsize
        for i in range(n):
            for j in range(m):
                if able_to_reach[i][j] == house_count:
                    min_total_steps = min(min_total_steps, min_dist_to_point[i][j])

        return min_total_steps if min_total_steps != sys.maxsize else -1

    def bfs(self, start_x, start_y, grid, min_dist_to_point, able_to_reach):
        DIRECTIONS = [
            (0, 1),
            (0, -1),
            (-1, 0),
            (1, 0)
        ]

        from collections import deque
        queue = deque([(start_x, start_y)])
        visited = set([(start_x, start_y)])

        min_dist_to_point[start_x][start_y] = sys.maxsize

        distance = -1

        while queue:
            distance += 1

            for _ in range(len(queue)):
                head = queue.popleft()
                min_dist_to_point[head[0]][head[1]] += distance
                able_to_reach[head[0]][head[1]] += 1

                x, y = head[0], head[1]

                for delta in DIRECTIONS:
                    x_new = x + delta[0]
                    y_new = y + delta[1]

                    if self.is_valid(x_new, y_new, grid, visited, min_dist_to_point):
                        queue.append((x_new, y_new))
                        visited.add((x_new, y_new))

    def is_valid(self, x, y, grid, visited, min_dist_to_point):
        if (x, y) in visited:
            return False

        n = len(grid)
        m = len(grid[0])

        if not (0 <= x < n and 0 <= y < m):
            return False

        if grid[x][y] == Category.HOUSE or grid[x][y] == Category.WALL:
            min_dist_to_point[x][y] = sys.maxsize
            return False

        return True


s = Solution()
grid = [[0,1,0,0,0],[1,0,0,2,1],[0,1,0,0,0]]
"""
010
101
010
"""
print(s.shortestDistance(grid))
