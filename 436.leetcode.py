"""
436. Find Right Interval
https://leetcode.com/problems/find-right-interval/
https://leetcode.com/problems/find-right-interval/discuss/91806/Python-O(nlogn)-short-solution-with-explanation
"""
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        starting_pt = sorted([(intervals[i][0], i) for i in range(n)]);
        res = [];
        for interval in intervals:
            r = bisect.bisect_left(starting_pt, (interval[1], ))
            res.append(starting_pt[r][1] if r != n else -1)
        return res
