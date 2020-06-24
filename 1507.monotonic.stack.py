"""
1507. Shortest Subarray with Sum at Least K

monotonic stack
"""
import sys
from collections import deque
class Solution:
    """
    @param A: the array
    @param K: sum
    @return: the length
    """
    def shortestSubarray(self, A, K):
        # Write your code here.
        if not A:
            return -1
        n = len(A)

        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + A[i - 1]

        queue = deque()
        
        min_len = sys.maxsize
        
        for i in range(n + 1):
            while queue and prefix_sum[i] - prefix_sum[queue[0]] >= K:
                min_len = min(min_len, i - queue.popleft())
            while queue and prefix_sum[queue[-1]] >= prefix_sum[i]: #because this prefix_sum index start at 1, and 
                queue.pop()
            queue.append(i)
        return min_len if min_len != sys.maxsize else -1