"""
49 · Sort Letters by Case
https://www.lintcode.com/problem/49/

standard partitioning template
"""
from typing import (
    List,
)

class Solution:
    """
    @param chars: The letter array you should sort by Case
    @return: nothing
    """
    def sort_letters(self, chars: List[str]):
        # write your code here
        if not chars:
            return chars

        l, r = 0, len(chars) - 1
        while l <= r:
            while l <= r and chars[l].islower():
                l += 1
            while l <= r and not chars[r].islower():
                r -= 1
            if l <= r:
                chars[l], chars[r] = chars[r], chars[l]
                l += 1
                r -= 1