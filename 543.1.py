"""
543. Kth Largest in N Arrays

https://www.lintcode.com/problem/kth-largest-in-n-arrays/

TLE

time complexity:
m list total, each list has on average n members;
then i have to do O(m*k + n*mlog(m))
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
        array_index = [0] * n

        heap = []

        while len(heap) < k:
            max_element, max_element_array = -sys.maxsize, None
            for i in range(n):
                if array_index[i] > len(arrays[i]) - 1:
                    continue
                if arrays[i][array_index[i]] > max_element:
                    max_element = arrays[i][array_index[i]]
                    max_element_array = i
            array_index[max_element_array] += 1
            heap.append(max_element)


        return heap[-1]
