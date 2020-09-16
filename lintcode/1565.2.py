"""
1565. Modern Ludo I
https://www.lintcode.com/problem/modern-ludo-i/description
bfs
九章算法高频题班
"""
import sys
from collections import deque
class Solution:
    """
    @param length: the length of board
    @param connections: the connections of the positions
    @return: the minimum steps to reach the end
    """
    def modernLudo(self, length, connections):
        transport = {}
        for start, end in connections:
            transport[start] = transport.get(start, set())
            transport[start].add(end)

        queue = deque([1])
        distance = {1:0}

        while queue:
            head = queue.popleft()
            for end in transport.get(head, set()):
                if end in distance and distance[end] < distance[head]:
                    continue
                queue.append(end)
                distance[end] = distance[head]
            for i in range(1, 7):
                next_pos = head + i
                if not self.is_valid(next_pos, length, distance):
                    continue
                queue.append(next_pos)
                distance[next_pos] = distance[head] + 1


        return distance[length]

    def is_valid(self, next_pos, length, distance):
        if next_pos < 0 or next_pos > length:
            return False
        if next_pos in distance:
            return False
        return True
