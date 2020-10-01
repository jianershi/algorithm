"""
104. Merge K Sorted Lists
https://www.lintcode.com/problem/merge-k-sorted-lists/description
o(k + knlogkn)
"""
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
import heapq
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    ListNode.__lt__ = lambda x, y : x.val < y.val
    
    def mergeKLists(self, lists):
        # write your code here
        k = len(lists)
        heap = []
        for root in lists:
            if root:
                heap.append(root)
        
        heapq.heapify(heap)
        
        # print(heap)
        dummy = ListNode(0)
        tail = dummy
        while heap:
            head = heapq.heappop(heap)
            tail.next = head
            tail = head
            if head.next:
                heapq.heappush(heap, head.next)

        return dummy.next
        
