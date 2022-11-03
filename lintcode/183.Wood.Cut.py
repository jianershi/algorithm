"""
183 · Wood Cut
https://www.lintcode.com/problem/183/

在结果上二分
"""

from typing import (
    List,
)

class Solution:
    """
    @param l: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def wood_cut(self, l: List[int], k: int) -> int:
        # write your code here
        if not l:
            return 0
        start, end = 0, max(l)
        while start < end:
            mid = (start + end + 1) // 2
            if self.canCut(l, mid, k):
                start = mid
            else:
                end = mid - 1
        
        return start

    def canCut(self, wood_list, cut_size, k):
        count = 0
        for wood in wood_list:
            count += wood // cut_size
        return count >= k