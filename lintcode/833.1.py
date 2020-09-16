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
        new_log = []
        for interval in logs:
            new_log.append((interval.start, 0))
            new_log.append((interval.end, 1))
            
        for i in queries:
            new_log.append((i, 2))
        
        new_log.sort()
        
        curr_sum = 0
        query_result = {}
        for i, status in new_log:
            if status == 0:
                curr_sum += 1
            elif status == 1:
                curr_sum -= 1
            
            if status == 2:
                query_result[i] = curr_sum

        return [query_result[x] for x in queries]
