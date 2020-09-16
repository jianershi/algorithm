"""
1691. Best Time to Buy and Sell Stock V

strategy:
put prices in priority queue,
if current price < heap[0], b < a that is a good price today consider we are selling at the highest possible price with lowest cost. sell.
but there might be a better price to sell later, so put the price back into the heap.
also save the current price in the heap again as possible buying prices.
when later price comes (c), we know immediately we should not sell. we should sell at c.
but that is not a problem since selling price is in the queue. (c - b) + (b - a) = c - a.
as if the selling never happend. it is also guaranteed now that b is no longer participated in the
previous sell, it is eligibal as a buying option. that is why b price was pushed into the queue twice.
the price price to track previous selling high prices in case higher prices comes later.
the other to track its buying prices in case it becomes eligibal to buy again.
when later prices is c < b. then it won't matter. because the next price is only going to worry about c.

"""
import sys
import heapq
class Solution:
    """
    @param a: the array a
    @return: return the maximum profit
    """
    def getAns(self, a):
        max_profit = 0
        heap = []
        for num in a:
            if heap and num > heap[0]:
                max_profit += num - heapq.heappop(heap)
                heapq.heappush(heap, num)
            heapq.heappush(heap, num)
        return max_profit

s = Solution()

a=[16,43,87,90]

print(s.getAns(a))
