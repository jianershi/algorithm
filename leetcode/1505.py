"""
1505. Minimum Possible Integer After at Most K Adjacent Swaps On Digits
https://leetcode.com/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/
https://leetcode.com/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/discuss/720650/Python-17-lines-O(nlogn)-solution
"""
from collections import deque, defaultdict
from string import digits
import bisect
class Solution:
    def minInteger(self, num: str, k: int) -> str:
        n = len(num)
        loc = defaultdict(deque)
        for i, c in enumerate(num):
            loc[c].append(i)
        ret, seen = "", []
        for _ in range(n):
            for c in digits:
                if loc[c]:
                    idx = loc[c][0]
                    shift = idx - bisect.bisect_right(seen, idx)
                    if shift <= k:
                        k -= shift
                        ret += c
                        bisect.insort_right(seen, loc[c].popleft())
                        break
        return ret