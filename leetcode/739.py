"""
739. Daily Temperatures
https://leetcode.com/problems/daily-temperatures/

monotonic stack (none-strict decreasing)
stack was only popped if new value is larger
"""
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n = len(T)
        res = [0] * n
        stack = []
        for i in range(n):
            while stack and T[stack[-1]] < T[i]:
                top = stack.pop()
                res[top] = i - top
            stack.append(i)
        return res