"""
1550. Three Consecutive Odds
https://leetcode.com/problems/three-consecutive-odds/
"""
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        for c in arr:
            if c % 2 == 1:
                count += 1
            else:
                count = 0
            if count == 3:
                return True
        return False