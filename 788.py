from collections import deque
class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: the shortest distance for the ball to stop at the destination
    """


    def shortestDistance(self, maze, start, destination):
        # write your code here
        DIRECTION_DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        if not maze:
            return -1
        visited = set([tuple(start)])
        memo = [[None] * len(maze[0]) for _ in range(len(maze))] #memo[i][j] = minimum length from i,j to dest
        min_dist = self.dfs(maze, tuple(start), DIRECTION_DELTA, tuple(destination), [], memo, visited)
        return min_dist if min_dist != sys.maxsize else - 1

    """
    recursively search 4 directions if able,
    return shortest length from this point to destination
    """
    def dfs(self, maze, start, DIRECTION_DELTA, destination, path, memo, visited):
        if start == destination:
            print ("path: %s" % path)
            memo[start[0]][start[1]] = 0
            return 0
        if memo[start[0]][start[1]]:
            return memo[start[0]][start[1]]

        min_dist = sys.maxsize
        for delta in DIRECTION_DELTA:
            x = start[0]
            y = start[1]
            new_steps = 0
            while not self.has_hit_wall(maze, (x, y)):
                x += delta[0]
                y += delta[1]
                new_steps += 1
            x -= delta[0]
            y -= delta[1]
            new_steps -= 1
            if new_steps == 0:
                continue
            if (x,y) in visited:
                continue
            visited.add((x, y))
            path.append((x,y))
            dfs_result = self.dfs(maze, (x, y), DIRECTION_DELTA, destination, path, memo, visited)

            if dfs_result != sys.maxsize:
                min_dist = min(min_dist, dfs_result + new_steps)
            visited.remove((x, y))
            path.pop()
        memo[start[0]][start[1]] = min_dist
        return min_dist

    def has_hit_wall(self, maze, next_location):
        num_row = len(maze)
        num_col = len(maze[0])

        next_r = next_location[0]
        next_c = next_location[1]

        if not (0 <= next_r < num_row):
            return True

        if not (0 <= next_c < num_col):
            return True

        if maze[next_r][next_c] == 1:
            return True

        return False
