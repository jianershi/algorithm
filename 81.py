"""
81. Find Median from Data Stream
https://www.lintcode.com/problem/find-median-from-data-stream/description
"""
import heapq
class Solution:
    """
    @param nums: A list of integers
    @return: the median of numbers
    """
    def medianII(self, nums):
        # write your code here
        max_heap = []
        min_heap = []
        results = []
        for num in nums:
            if max_heap and num <= -max_heap[0]:
                heapq.heappush(max_heap, -num)
            else:
                heapq.heappush(min_heap, num)
            self.balance(max_heap, min_heap)

            results.append(-max_heap[0])

        return results

    def balance(self, max_heap, min_heap):
        while len(max_heap) < len(min_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))

        while len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
