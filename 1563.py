from collections import deque
class Solution:
    """
    @param targetMap:
    @return: nothing
    """
    def shortestPath(self, targetMap):
        # Write your code here
        if not targetMap or not targetMap[0]:
            return -1

        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m = len(targetMap)
        n = len(targetMap[0])

        queue = deque([(0, 0)])
        visited = set([(0, 0)])

        depth = -1
        while queue:
            depth += 1
            for _ in range(len(queue)):
                head = queue.popleft()
                if targetMap[head[0]][head[1]] == 2:
                    return depth
                for delta in DIRECTIONS:
                    x, y = head
                    x += delta[0]
                    y += delta[1]
                    if self.is_valid(x, y, m, n, targetMap, visited):
                        queue.append((x, y))
                        visited.add((x, y))
        return -1

    def is_valid(self, x, y, m, n, map, visited):
        if (x, y) in visited:
            return False
        if not (0 <= x < m):
            return False
        if not (0 <= y < n):
            return False
        if map[x][y] == 1:
            return False
        return True

        
