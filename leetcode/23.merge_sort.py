"""
23. Merge k Sorted Lists
https://leetcode.com/problems/merge-k-sorted-lists/

104. Merge K Sorted Lists
https://www.lintcode.com/problem/merge-k-sorted-lists/description

merge sort

o(nlogk)
k: number of lists
n: total number of elements
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:  
        if not lists:
            return None
        return self.merge_lists(0, len(lists) - 1, lists)
    
    def merge_lists(self, start, end, lists):
        if start == end:
            return lists[start]
        
        mid = (start + end) // 2
        l = self.merge_lists(start, mid, lists)
        r = self.merge_lists(mid + 1, end, lists)
        return self.merge2lists(l, r)
        
    def merge2lists(self, l, r):
        dummy = ListNode(0)
        tail = dummy
        while l and r:
            if l.val < r.val:
                tail.next = l
                l = l.next
            else:
                tail.next = r
                r = r.next
            tail = tail.next
        
        if l:
            tail.next = l
            
        if r:
            tail.next = r
            
        return dummy.next