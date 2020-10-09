"""
23. Merge k Sorted Lists
https://leetcode.com/problems/merge-k-sorted-lists/

104. Merge K Sorted Lists
https://www.lintcode.com/problem/merge-k-sorted-lists/description

heap

o(k + nlogk)
k: number of lists
n: total number of elements
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def cmp(x, y):
        return x.val < y.val
    # ListNode.__lt__ = lambda x, y: x.val < y.val
    ListNode.__lt__ = cmp

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:  
        if not lists:
            return None
        
        heap = []
        for root in lists:
            if root:
                heap.append(root)
        
        heapq.heapify(heap)
        
        dummy = ListNode()
        tail = dummy
        while heap:
            top = heapq.heappop(heap)
            tail.next = top
            tail = top
            if top.next:
                heapq.heappush(heap, top.next)
        
        return dummy.next