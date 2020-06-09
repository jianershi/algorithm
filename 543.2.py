"""
543. Kth Largest in N Arrays

https://www.lintcode.com/problem/kth-largest-in-n-arrays/

time complexity:
m list total, each list has on average n members;
to sort each array O(m*nlogn)
to add first element O(m)
to add next k element, each pop and push combination o(logm) * 2, need to do k times
total O(m*nlogn + m + klogm)

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
        for arr in arrays:
            arr.sort(reverse=True)

        n = len(arrays)

        index_in_array = [1] * n

        max_heap = []

        for i in range(n):
            if len(arrays[i]) == 0:
                continue
            heapq.heappush(max_heap, (-arrays[i][0], i))

        for _ in range(k):
            negative_max_element, array_i = heapq.heappop(max_heap)
            if index_in_array[array_i] > len(arrays[array_i]) -1:
                continue
            heapq.heappush(max_heap, (-arrays[array_i][index_in_array[array_i]], array_i))
            index_in_array[array_i] += 1
        return -negative_max_element
