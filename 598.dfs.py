"""
598. Zombie in Matrix
dfs
if visited, check if the current path length is shorter than recorded.
you will also not be able to modify the matrix as you go as multi-starting point
BFS solution because in BFS, you are sure current step is indeed the shortest way
to reach here. in DFS, you are not sure.

**this will exceed timelimit.**

"""
import sys
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

        step_count = [[sys.maxsize] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == Category.ZOMBIE:
                    step_count[i][j] = 0 #zombie only need 0 steps to become zombie
                    self.dfs(grid, i, j, set([(i, j)]), step_count)

        # self.print_matrix(step_count)

        max_steps = -sys.maxsize
        for i in range(m):
            for j in range(n):
                if step_count[i][j] == sys.maxsize and grid[i][j] == Category.HUMAN: #has zombie
                    return -1
                if grid[i][j] == Category.HUMAN:
                    max_steps = max(max_steps, step_count[i][j])

        return max_steps

    def dfs(self, grid, i, j, path, step_count):
        DIRECTIONS = [
            (0, 1),
            (0, -1),
            (-1, 0),
            (1, 0)
        ]
        for direction in DIRECTIONS:
            x = i + direction[0]
            y = j + direction[1]
            if self.is_valid(grid, x, y, len(path), path, step_count):
                path.add((x, y))
                step_count[x][y] = len(path) - 1
                self.dfs(grid, x, y, path, step_count)
                path.remove((x, y))
        return

    def is_valid(self, grid, x, y, steps_to_x_y, path, step_count):
        m = len(grid)
        n = len(grid[0])

        """
        hitting itself in current route
        """
        if (x, y) in path:
            return False

        if not (0 <= x < m and 0 <= y < n):
            return False

        if grid[x][y] == Category.ZOMBIE or grid[x][y] == Category.WALL:
            return False

        """
        only have to continue seraching if current steps_to_x_y < recorded minimum steps
        at this location.
        """
        if step_count[x][y] <= steps_to_x_y:
            return False

        step_count[x][y] = steps_to_x_y
        return True

    """
    for debugging purpose
    """
    def print_matrix(self, matrix):
        for i in matrix:
            print (i)

# s = Solution()
# grid = [[0,1,2,0,0],[1,0,0,2,1],[0,1,0,0,0]]
# print(s.zombie(grid))
