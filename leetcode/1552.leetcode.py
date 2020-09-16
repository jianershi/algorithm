"""
1552. Magnetic Force Between Two Balls
https://leetcode.com/contest/weekly-contest-202/problems/magnetic-force-between-two-balls/
"""
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position = sorted(position)
        start, end = 1, position[-1]
        while start + 1 < end:
            mid = (start + end) // 2
            if self.is_ok(mid, position, m):
                start = mid
            else:
                end = mid
        if self.is_ok(end, position, m):
            return end
        return start

    def is_ok(self, min_dist, position, m):
        i = 1
        n = len(position)
        m -= 1
        last_position = position[0]
        while m > 0:
            while i < n and position[i] - last_position < min_dist:
                i += 1
            if i < n:
                last_position = position[i]
                m -= 1
            if m <= 0:
                return True
            if i == n:
                return False
        if m <= 0:
            return True
        return False