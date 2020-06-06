"""
573. Build Post Office II
You cannot pass through wall and house, but can pass through empty.
You only build post office on an empty.

time limit exceeded
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


        house_locations = []
        empty_locations = []

        for i in range(n):
            for j in range(m):
                if grid[i][j] == Category.HOUSE:
                    house_locations.append((i,j))
                if grid[i][j] == Category.EMPTY:
                    empty_locations.append((i, j))

        # print(house_locations, empty_locations)
        min_total_steps = sys.maxsize

        for empty_space_i, empty_space_j in empty_locations:
            total_steps = 0
            for house_i, house_j in house_locations:
                steps = self.bfs(house_i, house_j, empty_space_i, empty_space_j, grid)
                if steps == -1:
                    total_steps = sys.maxsize
                    break
                # print (house_i, house_j, empty_space_i, empty_space_j, steps)
                """
                [0,1,0]
                [1,0,1]
                [0,1,0]

                """
                total_steps += steps
            min_total_steps = min(min_total_steps, total_steps)

        return min_total_steps if min_total_steps != sys.maxsize else -1

    def bfs(self, start_x, start_y, end_x, end_y, grid):
        DIRECTIONS = [
            (0, 1),
            (0, -1),
            (-1, 0),
            (1, 0)
        ]

        from collections import deque
        queue = deque([(start_x, start_y)])
        visited = set([(start_x, start_y)])

        distance = -1

        while queue:
            distance += 1

            for _ in range(len(queue)):
                head = queue.popleft()

                if head == (end_x, end_y):
                    return distance

                x, y = head[0], head[1]

                for delta in DIRECTIONS:
                    x_new = x + delta[0]
                    y_new = y + delta[1]

                    if self.is_valid(x_new, y_new, grid, visited):
                        queue.append((x_new, y_new))
                        visited.add((x_new, y_new))

        return -1

    def is_valid(self, x, y, grid, visited):
        if (x, y) in visited:
            return False

        n = len(grid)
        m = len(grid[0])

        if not (0 <= x < n and 0 <= y < m):
            return False

        if grid[x][y] == Category.HOUSE or grid[x][y] == Category.WALL:
            return False

        return True


s = Solution()
grid = [[0,1,0,0,0],[1,0,0,2,1],[0,1,0,0,0]]
print(s.shortestDistance(grid))
