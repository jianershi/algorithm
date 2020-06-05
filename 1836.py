"""
1836. Reaching Point
Example 1:
Input:
start = [1, 1]
target = [5, 2]
Output: True
Explanation: (1, 1) -> (1, 2) -> (3, 2) -> (5, 2)

BFS. Memory Limited Exceeded
"""
from collections import deque
class Solution:
    """
    @param start: a point [x, y]
    @param target: a point [x, y]
    @return: return True or False
    """
    def ReachingPoints(self, start, target):
        # write your code here
        if not start or not target:
            return False
        if start == target:
            return True

        queue = deque([tuple(start)])

        # don't need visited because it can not form circle

        while queue:
            head = queue.popleft()
            if head == tuple(target):
                return True
            x, y = head[0], head[1]
            x_1, y_1 = x + y, y
            x_2, y_2 = x, x + y
            if x_1 <= target[0] and y_1 <= target[1]:
                queue.append((x_1, y_1))
            if x_2 <= target[0] and y_2 <= target[1]:
                queue.append((x_2, y_2))

        return False


s = Solution()
start = [1, 2]
target =[99840,40832]
print(s.ReachingPoints(start, target))
