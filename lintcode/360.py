"""
360. Sliding Window Median
https://www.lintcode.com/problem/sliding-window-median/description
J's method: https://www.jiuzhang.com/solution/sliding-window-median/#tag-other-lang-python
"""
import heapq
class Heap:
    def __init__(self):
        self.heap = []
        self.deleted = {}
        self.length = 0

    def push(self, element):
        heapq.heappush(self.heap, element)
        self.length += 1

    def pop(self):
        self.remove_redundant()
        self.length -= 1
        return heapq.heappop(self.heap)

    def remove(self, element):
        self.deleted[element] = self.deleted.get(element, 0) + 1
        self.length -= 1

    def remove_redundant(self):
        while self.heap and self.deleted.get(self.heap[0]):
            removed_duplicate = heapq.heappop(self.heap)
            self.deleted[removed_duplicate] -= 1
            if self.deleted[removed_duplicate] == 0:
                del self.deleted[removed_duplicate]

    def peek(self):
        self.remove_redundant()
        return self.heap[0]

    def __len__(self):
        return self.length

    def __repr__(self):
        return repr(self.heap)

class Solution:
    """
    @param nums: A list of integers
    @param k: An integer
    @return: The median of the element inside the window at each moving
    """
    def medianSlidingWindow(self, nums, k):
        # write your code here
        max_heap = Heap()
        min_heap = Heap()
        removed_elements = set()

        right = 0
        results = []
        n = len(nums)
        for left in range(n):
            while right < n and right - left < k:
                if len(max_heap) == 0 or nums[right] <= -max_heap.peek():
                    max_heap.push(-nums[right])
                else:
                    min_heap.push(nums[right])
                self.balance(max_heap, min_heap)
                right += 1

            if right - left == k:
                results.append(-max_heap.peek())
            if right >= n:
                break;

            if nums[left] <= -max_heap.peek():
                max_heap.remove(-nums[left])
            else:
                min_heap.remove(nums[left])
            self.balance(max_heap, min_heap)

        return results

    def balance(self, max_heap, min_heap):
        while len(max_heap) < len(min_heap):
            max_heap.push(-min_heap.pop())

        while len(max_heap) > len(min_heap) + 1:
            min_heap.push(-max_heap.pop())
