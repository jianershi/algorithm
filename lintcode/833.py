"""
833. Process Sequence
sweeping line
"""
"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import sys
class Solution:
    """
    @param logs: Sequence of processes
    @param queries: Sequence of queries
    @return: Return the number of processes
    """
    def numberOfProcesses(self, logs, queries):
        # Write your code here
        # min_time = min(logs, key = lambda x: x.start)
        min_time = sys.maxsize
        max_time = 0
        logs = sorted(logs, key=lambda x : (x.start, x.end))
        for interval in logs:
            min_time = min(min_time, interval.start)
            max_time = max(max_time, interval.end)
            
        line = [0] * (max_time - min_time + 1)
        for interval in logs:
            line[interval.start - min_time] += 1
            line[interval.end - min_time] -= 1

        prefix_sum = []
        curr_sum = 0

        for i in line:
            curr_sum += i
            prefix_sum.append(curr_sum)

        ret = []
        for i in queries:
            ret.append(prefix_sum[i - min_time])

        return ret
