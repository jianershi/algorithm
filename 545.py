import heapq
class Solution:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        # do intialization if necessary
        self.heap = []
        self.k = k
    """
    @param: num: Number to be added
    @return: nothing
    """
    def add(self, num):
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, num)
            return
        next_number_to_push = (self.heap, max(heapq.heappop(self.heap), num))
        heapq.heappush(self.heap, next_number_to_push)
    """
    @return: Top k element
    """
    def topk(self):
        # write your code here
        return sorted(self.heap, reverse=True)


s = Solution(3)
print(s.add(3))
print(s.add(10))
print(s.topk())
print(s.add(1000))
print(s.add(-99))
print(s.topk())
print(s.add(4))
print(s.topk())
print(s.add(100))
print(s.topk())
