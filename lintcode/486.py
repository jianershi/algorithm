"""
486. Merge K Sorted Arrays
https://www.lintcode.com/problem/merge-k-sorted-arrays/description
"""
import heapq
class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        # write your code here
        heap = []
        for arr_index, arr in enumerate(arrays):
            if arr != []:
                heapq.heappush(heap, (arr[0], arr_index, 0))

        n = len(arrays)

        results = []
        while len(heap) > 0:
            num, arr_i, i = heapq.heappop(heap)
            results.append(num)
            if i + 1 > len(arrays[arr_i]) - 1:
                continue
            heapq.heappush(heap, (arrays[arr_i][i + 1], arr_i, i + 1))
        return results

s = Solution()
arrays = [[1,3,5,7],[2,4,6],[0,8,9,10,11]]
print(s.mergekSortedArrays(arrays))
