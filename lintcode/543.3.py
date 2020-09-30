"""
543. Kth Largest in N Arrays
https://www.lintcode.com/problem/kth-largest-in-n-arrays/

TLE

suppose each array is of length n, of total N arrays
sort each array: O(nlogn * N) large->small
find largest from top of each array O(N) * O(logk) insert into heap * K total k times
find kth largest O(1) <- since it is max heap
total time complexity : O(Nnlogn + KNlogK)
"""
import heapq
class Solution:
    """
    @param arrays: a list of array
    @param k: An integer
    @return: an integer, K-th largest element in N arrays
    """
    def KthInArrays(self, arrays, k):
        # write your code here
        n = len(arrays)
        pt = [0] * n
        for i in range(n):
            arrays[i].sort(reverse = True)
        
        res = []
        for _ in range(k):
            max_element, max_idx = -sys.maxsize, -1
            for i in range(n):
                if pt[i] < len(arrays[i]) and arrays[i][pt[i]] > max_element:
                    max_element, max_idx = arrays[i][pt[i]], i
            pt[max_idx] += 1
            heapq.heappush(res, -max_element)
            
        return -res[-1]