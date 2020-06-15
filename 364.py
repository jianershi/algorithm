"""
364. Trapping Rain Water II
https://www.lintcode.com/problem/trapping-rain-water-ii/description

magic barrier, attack on titan algorithm.
"""
import heapq
DIRECTIONS = [
    (0, 1),
    (0, -1),
    (-1, 0),
    (1, 0)
]
class Solution:
    """
    @param heights: a matrix of integers
    @return: an integer
    """
    def trapRainWater(self, heights):
        # write your code here
        if not heights or not heights[0]:
            return 0

        n = len(heights)
        m = len(heights[0])

        min_heap = [] # height of location, (x, y)
        visited = set()
        water_capacity = 0

        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0 or i == n - 1 or j == m - 1:
                    heapq.heappush(min_heap, (heights[i][j], (i, j)))
                    visited.add((i, j))

        while min_heap:
            lowest_blocking_height, (x, y) = heapq.heappop(min_heap)
            for delta in DIRECTIONS:
                next_x = x + delta[0]
                next_y = y + delta[1]
                if self.is_valid(n, m, next_x, next_y, visited):
                    next_height = max(heights[next_x][next_y], lowest_blocking_height)
                    water_capacity += max(0, lowest_blocking_height - heights[next_x][next_y])
                    heapq.heappush(min_heap, (next_height, (next_x, next_y)))
                    visited.add((next_x, next_y))
        return water_capacity

    def is_valid(self, n, m, next_x, next_y, visited):
        if (next_x, next_y) in visited:
            return False
        if next_x < 0 or next_x >= n or next_y < 0 or next_y >= m:
            return False
        return True
