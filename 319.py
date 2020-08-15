"""
319. Square Queue
https://www.lintcode.com/problem/square-queue/description
"""
import math
class Solution:
    """
    @param height: n people's height
    @return: return the maxium number of people in square matrix
    """
    def MaxPeopleNumber(self, height):
        # write your code here
        height = sorted(height)
        max_per_group = int(math.sqrt(len(height)))
        start, end = 1, max_per_group
        while start + 1 < end:
            mid = (start + end) // 2
            if self.is_ok(mid, height):
                start = mid
            else:
                end = mid
        if self.is_ok(end, height):
            return end ** 2
        else:
            return start ** 2
    
    def is_ok(self, window_size, height):
        l = 0
        r = 0
        min_window = height[0]
        max_windw = height[0]
        n = len(height)
        row = 0
        while l <= n - window_size:
            min_window = height[l]
            while r < n and r - l < window_size:
                max_window = height[r]
                if abs(height[r] - min_window) > 2 or abs(height[r] - max_window) > 2:
                    r += 1
                    l += 1
                    min_window = height[l]
                else:
                    r += 1
            if r - l == window_size:
                row += 1
                l = r - 1
            l += 1
        if row >= window_size:
            return True
        return False

s = Solution()
height = [2,5,4,5]
print(s.MaxPeopleNumber(height))
            
