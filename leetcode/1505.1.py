"""
1505. Minimum Possible Integer After at Most K Adjacent Swaps On Digits
https://leetcode.com/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/
https://leetcode.com/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/discuss/720650/Python-17-lines-O(nlogn)-solution
"""
from collections import deque
from string import digits

class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.t = [0] * (4 * n)
        
    def insert(self, v, tl, tr, pos) :
        if tl == tr:
            self.t[v] += 1
            return
        tm = (tl + tr) // 2
        if pos <= tm:
            self.insert(v * 2, tl, tm, pos)
        else:
            self.insert(v * 2 + 1, tm + 1, tr, pos)
        self.t[v] = self.t[v * 2] + self.t[v * 2 + 1]
        
    def query(self, v, tl, tr, l, r):
        if l > r:
            return 0
        if tl == l and tr == r:
            return self.t[v]
        tm = (tl + tr) // 2
        return self.query(v * 2, tl, tm, l, min(r, tm)) + self.query(v * 2 + 1, tm + 1, tr, max(l, tm + 1), r)
        
class Solution:
    def minInteger(self, num, k):
        n = len(num)
        loc = defaultdict(deque)
        for i, c in enumerate(num):
            loc[c].append(i)
        ret, sg = "", SegmentTree(n)
        for _ in range(n):
            for c in digits:
                if loc[c]:
                    idx = loc[c][0]
                    shift = idx - sg.query(1, 0, n - 1, 0, idx)
                    if shift <= k:
                        k -= shift
                        ret += c
                        sg.insert(1, 0, n - 1, int(loc[c].popleft()))
                        break
        return ret