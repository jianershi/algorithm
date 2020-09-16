"""
1565. Modern Ludo I
https://www.lintcode.com/problem/modern-ludo-i/description
dp[i] min steps to this point.
九章算法高频题班
"""
import sys
class Solution:
    """
    @param length: the length of board
    @param connections: the connections of the positions
    @return: the minimum steps to reach the end
    """
    def modernLudo(self, length, connections):
        # Write your code here
        dp = [sys.maxsize] * (length + 1) #? why + 1
        transport = {}
        for start, end in connections:
            transport[end] = transport.get(end, set())
            transport[end].add(start)

        dp[1] = 0

        for i in range(2, length + 1):
            for j in range(1, 7):
                if i - j < 0:
                    continue
                dp[i] = min(dp[i], dp[i - j] + 1)
            if i not in transport:
                continue
            for start in transport[i]:
                dp[i] = min(dp[i], dp[start])

        return dp[length]
