"""
1272. Kth Smallest Element in a Sorted Matrix
https://www.lintcode.com/problem/kth-smallest-element-in-a-sorted-matrix/description
"""
import heapq
class Solution:
    """
    @param matrix: List[List[int]]
    @param k: a integer
    @return: return a integer
    """
    def kthSmallest(self, matrix, k):
        # write your code here
        if not matrix or not matrix[0]:
            return matrix

        heap = [(matrix[0][0], (0, 0))]
        DIRECTIONS = [
            (0, 1),
            (1, 0)
        ]
        visited = set((0, 0))
        for _ in range(k):
            num, (x, y) = heapq.heappop(heap)
            for delta in DIRECTIONS:
                new_x = x + delta[0]
                new_y = y + delta[1]
                if self.is_valid(matrix, new_x, new_y, visited):
                    heapq.heappush(heap, (matrix[new_x][new_y], (new_x, new_y)))
                    visited.add((new_x, new_y))
        return num

    def is_valid(self, matrix, x, y, visited):
        n = len(matrix)
        m = len(matrix[0])

        if (x, y) in visited:
            return False

        if not (0 <= x < n and 0 <= y < m):
            return False

        return True
