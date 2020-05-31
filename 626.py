"""
626. Rectangle Overlap
too many over lapping cases. instead, solving not overlapping cases.
"""
"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param l1: top-left coordinate of first rectangle
    @param r1: bottom-right coordinate of first rectangle
    @param l2: top-left coordinate of second rectangle
    @param r2: bottom-right coordinate of second rectangle
    @return: true if they are overlap or false
    """
    def doOverlap(self, l1, r1, l2, r2):
        # write your code here
        return not self.check_not_overlap(l1, r1, l2, r2)

    def check_not_overlap(self, l1, r1, l2, r2):
        #four directions only
        if l1.x < r1.x < l2.x < r2.x:
            return True
        if l2.x < r2.x < l1.x < r1.x:
            return True
        if r1.y < l1.y < r2.y < l2.y:
            return True
        if r2.y < l2.y < r1.y < l1.y:
            return True
        return False
