"""
543. Kth Largest in N Arrays
https://www.lintcode.com/problem/kth-largest-in-n-arrays/

TLE

suppose each array is of length n, of total N arrays
sort each array: O(nlogn * N) large->small
insert all list into heap O(N) + heapify O(N)
remove the largest and insert the next element, O(logN)

total time complexity : O(Nnlogn + N + KlogN)
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
        for arr in arrays:
            arr.sort(reverse = True)
        
        heap = []
        for i in range(n):
            if pt[i] < len(arrays[i]):
                heap.append((-arrays[i][pt[i]], i))
        heapq.heapify(heap)
        
        for _ in range(k):
            neg_max, arr_idx = heapq.heappop(heap)
            pt[arr_idx] += 1
            if pt[arr_idx] < len(arrays[arr_idx]):
                heapq.heappush(heap, (-arrays[arr_idx][pt[arr_idx]], arr_idx))
            
        return -neg_max