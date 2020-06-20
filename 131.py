"""
131. The Skyline Problem
https://www.lintcode.com/problem/the-skyline-problem/description
"""
import heapq
class Heap:
    def __init__(self):
        self.heap = []
        self.deleted = {}
        self.count = 0

    def push(self, x):
        heapq.heappush(self.heap, x)
        self.count += 1

    def peek(self):
        while self.heap and self.deleted.get(self.heap[0], 0):
            self.deleted[self.heap[0]] -= 1
            if self.deleted[self.heap[0]] == 0:
                del self.deleted[self.heap[0]]
            heapq.heappop(self.heap)

        return self.heap[0] if self.heap else None

    def pop(self):
        top = self.peek()
        if top is None:
            return None
        heapq.heappop(self.heap)
        self.count -= 1
        return top

    def delete(self, x):
        self.deleted[x] = self.deleted.get(x, 0) + 1
        self.count -= 1

class Event:
    UP = 0
    DOWN = 1

class Solution:
    """
    @param buildings: A list of lists of integers
    @return: Find the outline of those buildings
    """
    def buildingOutline(self, buildings):
        # write your code here
        list = []
        for start, end, height in buildings:
            list.append((start, Event.UP, height))
            list.append((end, Event.DOWN, height))
        list.sort()

        heap = Heap() #height
        results = []
        combined_results = []
        last_height = None #last height
        for i in range(len(list)):
            time, event, height = list[i]
            if event == Event.UP:
                heap.push(-height)
            else:
                heap.delete(-height)

            if i + 1 != len(list) and list[i + 1][0] == time:
                continue
            if last_height is not None and last_height == (-heap.peek() if heap.count else 0):
                continue
            if results:
                starting_time = results[-1][0]
                ending_time = time
                range_height = results[-1][1]
                if range_height > 0:
                    combined_results.append([starting_time, ending_time, range_height])
            last_height = -heap.peek() if heap.count else 0
            results.append([time, last_height])

        return combined_results

s = Solution()
buildings = [[1,3,3],[2,4,4],[5,6,1]]
"""
133
"""

print(s.buildingOutline(buildings))
