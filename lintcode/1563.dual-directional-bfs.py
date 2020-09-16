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


        queue1 = deque([(0, 0)])
        target_index = self.find_target(targetMap)
        print("target: (%s,%s)" % (target_index[0], target_index[1]))
        if target_index == (-1, -1):
            return -1
        queue2 = deque([target_index])
        visited = {(0, 0): 1, target_index: 2}

        depth = -1

        while queue1 or queue2:
            if queue1:
                depth += 1
                is_found = self.process_queue(queue1, visited, targetMap, 1)
                if is_found:
                    return depth
            if queue2:
                depth += 1
                is_found = self.process_queue(queue2, visited, targetMap, 2)
                if is_found:
                    return depth
        return -1

    def process_queue(self, queue, visited, targetMap, flag):
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m = len(targetMap)
        n = len(targetMap[0])
        for _ in range(len(queue)):
            head = queue.popleft()
            if visited[head] != flag:
                return True
            for delta in DIRECTIONS:
                x, y = head
                x += delta[0]
                y += delta[1]
                if not self.is_valid(x, y, m, n, targetMap):
                    continue
                if (x, y) in visited and visited[(x, y)] == flag:
                    continue
                queue.append((x, y))
                visited[(x, y)] = flag #update flag
        return False

    def is_valid(self, x, y, m, n, map):
        if not (0 <= x < m):
            return False
        if not (0 <= y < n):
            return False
        if map[x][y] == 1:
            return False
        return True

    def find_target(self, map):
        m = len(map)
        n = len(map[0])
        for i in range(m):
            for j in range(n):
                if map[i][j] == 2:
                    return i, j
        return -1, -1

s = Solution()
targetMap = [
 [0, 0, 0],
 [0, 0, 1],
 [0, 0, 2]
]
print(s.shortestPath(targetMap))
