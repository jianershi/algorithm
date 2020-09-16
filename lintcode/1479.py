"""
1479. Can Reach The Endpoint
https://www.lintcode.com/problem/can-reach-the-endpoint/description
"""
from collections import deque
DIRECTIONS = [
    (0, 1),
    (0, -1),
    (-1, 0),
    (1, 0)
]
class DataType:
    ENDPOINT = 9
    OBSTACLE = 0

class Solution:
    """
    @param map: the map
    @return: can you reach the endpoint
    """
    def reachEndpoint(self, map):
        # Write your code here
        if not map or not map[0]:
            return False

        queue = deque([(0, 0)])
        visited = set([(0, 0)])

        while queue:
            x, y = queue.popleft()
            for delta in DIRECTIONS:
                next_x = x + delta[0]
                next_y = y + delta[1]
                if not self.is_valid(next_x, next_y, map, visited):
                    continue
                if map[next_x][next_y] == DataType.ENDPOINT:
                    return True
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))
        return False

    def is_valid(self, x, y, map, visited):
        n = len(map)
        m = len(map[0])

        if (x, y) in visited:
            return False
        if not (0 <= x < n and 0 <= y < m):
            return False
        if map[x][y] == DataType.OBSTACLE:
            return False

        return True
