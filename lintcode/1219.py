"""
1219. Heaters
https://www.lintcode.com/problem/heaters/description
"""
import sys
class Solution:
    """
    @param houses: positions of houses
    @param heaters: positions of heaters
    @return: the minimum radius standard of heaters
    """
    def findRadius(self, houses, heaters):
        # Write your code here
        min_radius = -sys.maxsize
        heaters.sort()
        for house in houses:
            min_radius = max(min_radius, self.binary_search(house, heaters))
        return min_radius if min_radius != sys.maxsize else -1

    def binary_search(self, house, heaters):
        start, end = 0, len(heaters) - 1
        min_distance = sys.maxsize
        while start + 1 < end:
            mid = (start + end) // 2
            if house < heaters[mid]:
                end = mid
            if house > heaters[mid]:
                start = mid
            if house == heaters[mid]:
                return 0
        min_distance = min(min_distance, abs(house - heaters[start]), abs(heaters[end] - house))
        return min_distance
        
s = Solution()
houses, heaters = [1,2,3,4],[1,4]
print(s.findRadius(houses, heaters))
