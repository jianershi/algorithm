"""
23. Merge k Sorted Lists
https://leetcode.com/problems/merge-k-sorted-lists/

104. Merge K Sorted Lists
https://www.lintcode.com/problem/merge-k-sorted-lists/description

merge 2 neighbors

o(klogn)
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
        
        current_lists = lists
        while len(current_lists) > 1:
            next_list = []
            for i in range(0, len(current_lists), 2):
                if i + 1 < len(current_lists):
                    next_list.append(self.merge2lists(current_lists[i], current_lists[i + 1]))
                else:
                    next_list.append(current_lists[i])
            current_lists = next_list
        return current_lists[0]
        
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