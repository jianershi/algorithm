"""
465. Kth Smallest Sum In Two Sorted Arrays
https://www.lintcode.com/problem/kth-smallest-sum-in-two-sorted-arrays/description
similar to 1272
"""
import heapq
class Solution:
    """
    @param A: an integer arrays sorted in ascending order
    @param B: an integer arrays sorted in ascending order
    @param k: An integer
    @return: An integer
    """
    def kthSmallestSum(self, A, B, k):
        # write your code here
        DIRECTIONS = [
            (0, 1),
            (1, 0)
        ]
        if not A and not B:
            return None
        if not A:
            return B[0]
        if not B:
            return A[0]

        n = len(A)
        m = len(B)

        heap = [(A[0] + B[0], (0, 0))]
        visited = set((0, 0))

        for _ in range(k):
            num, (x, y) = heapq.heappop(heap)
            for delta in DIRECTIONS:
                new_x, new_y = x + delta[0], y + delta[1]
                if self.is_valid(n, m, new_x, new_y, visited):
                    visited.add((new_x, new_y))
                    heapq.heappush(heap, (A[new_x] + B[new_y], (new_x, new_y)))
        return num

    def is_valid(self, n, m, x, y, visited):
        if (x, y) in visited:
            return False

        if not (0 <= x < n and 0 <= y < m):
            return False

        return True
