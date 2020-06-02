"""
788. The Maze II
updated with comment
"""
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
        queue = deque([tuple(start)])
        #min_dist_to_point: minimum distance to position key from start as value.
        #e.x. min_dist_to_point[(3, 2)] = 2 minimum distance to location (3, 2) si 2
        #this also servers as visited.
        min_dist_to_point = {tuple(start): 0}


        while queue:
            head = queue.popleft()
            for delta in DIRECTION_DELTA:
                x = head[0] + delta[0]
                y = head[1] + delta[1]
                steps = 1
                while not self.has_hit_wall(maze, (x, y)):
                    x += delta[0]
                    y += delta[1]
                    steps += 1
                x -= delta[0]
                y -= delta[1]
                steps -= 1
                if (x, y) in min_dist_to_point: #that means the point was previously visited
                    if min_dist_to_point[head] + steps < min_dist_to_point[(x, y)]:
                        queue.append((x, y)) #re-append to the queue if the current solution result in smallest distance
                        min_dist_to_point[(x, y)] = min_dist_to_point[head] + steps
                else: # if the point was not previously visited, append to the queue
                    queue.append((x, y))
                    min_dist_to_point[(x, y)] = min_dist_to_point[head] + steps
        return min_dist_to_point[tuple(destination)] if tuple(destination) in min_dist_to_point else -1


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
