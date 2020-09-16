"""
1364. the minium distance
https://www.lintcode.com/problem/the-minium-distance/description?_from=ladder&&fromId=160

prebuilt a map for gateways
"""
class DataType:
    START_POINT = -2
    END_POINT = -3
    OBSTACLE = -1

from collections import deque
DIRECTIONS = [
    (0, 1),
    (0, -1),
    (-1, 0),
    (1, 0)
]
class Solution:
    """
    @param mazeMap: a 2D grid
    @return: return the minium distance
    """
    def getMinDistance(self, mazeMap):
        # write your code here
        if not mazeMap or not mazeMap[0]:
            return mazeMap

        start_loc, gateway_location = self.build_value_map(mazeMap)
        queue = deque([(start_loc,0)])
        visited = set([start_loc])
        gateway_used = set()

        while queue:
            (x, y), dist = queue.popleft()
            for delta_x, delta_y in DIRECTIONS:
                next_x = x + delta_x
                next_y = y + delta_y
                if self.is_valid(mazeMap, next_x, next_y, visited):
                    if mazeMap[next_x][next_y] == DataType.END_POINT:
                        return dist + 1
                    if mazeMap[next_x][next_y] > 0 and mazeMap[next_x][next_y] in gateway_used:
                        continue
                    queue.append(((next_x, next_y), dist + 1))
                    visited.add((next_x, next_y))
            if mazeMap[x][y] <= 0 or mazeMap[x][y] in gateway_used:
                continue
            for jump_to_x, jump_to_y in gateway_location[mazeMap[x][y]]:
                if self.is_jump_point_valid(mazeMap, x, y, jump_to_x, jump_to_y, visited):
                    if mazeMap[jump_to_x][jump_to_y] == DataType.END_POINT:
                        return dist + 1
                    queue.append(((jump_to_x, jump_to_y), dist + 1))
                    visited.add((jump_to_x, jump_to_y))
            gateway_used.add(mazeMap[x][y])
        return -1

    def is_jump_point_valid(self, mazeMap, x, y, jump_to_x, jump_to_y, visited):
        if (jump_to_x, jump_to_y) in visited:
            return False
        if mazeMap[x][y] <= 0:
            return False

        return mazeMap[jump_to_x][jump_to_y] == mazeMap[x][y]

    def is_valid(self, mazeMap, next_x, next_y, visited):
        if (next_x, next_y) in visited:
            return False
        n = len(mazeMap)
        m = len(mazeMap[0])
        if not (0 <= next_x < n and 0 <= next_y < m):
            return False
        if mazeMap[next_x][next_y] == DataType.START_POINT:
            return False
        if mazeMap[next_x][next_y] == DataType.OBSTACLE:
            return False
        return True

    def build_value_map(self, mazeMap):
        start_point = None
        gateway_location = {}
        n = len(mazeMap)
        m = len(mazeMap[0])
        for i in range(n):
            for j in range(m):
                if mazeMap[i][j] == DataType.START_POINT:
                    start_point = (i, j)
                if mazeMap[i][j] <= 0:
                    continue
                gateway_location[mazeMap[i][j]] = gateway_location.get(mazeMap[i][j], set())
                gateway_location[mazeMap[i][j]].add((i, j))
        return (start_point, gateway_location)
