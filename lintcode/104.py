"""
104. Merge K Sorted Lists
https://www.lintcode.com/problem/merge-k-sorted-lists/description
"""
import heapq
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
"""
方法1
拿出头，然后分别比。时间复杂度O(NlogK)
K代表priority queue的长度
N是所有的节点的个数
"""
# # def ListNodeLessThan(a, b):
#     # return a.val < b.val
# # ListNode.__lt__ = ListNodeLessThan
# ListNode.__lt__ = lambda x, y : x.val < y.val

# class Solution:
#     """
#     @param lists: a list of ListNode
#     @return: The head of one sorted list.
#     """
#     def mergeKLists(self, lists):
        
#         # write your code here
#         heap =  []
#         dummy = ListNode(0)
#         tail = dummy
#         for head_node in lists:
#             if head_node:
#                 heapq.heappush(heap, head_node)
        
#         while heap:#时间复杂度O(N)
#             head = heapq.heappop(heap) #O(logK)
#             tail.next = head
#             tail = head
#             if head.next:
#                 heapq.heappush(heap, head.next) #O(logK)
        
#         return dummy.next

"""
方法2:
用分治法merge sort的思路做
merge sort 
树高logK
每层都需要耗费O(N)合并
"""
# class Solution:
#     """
#     @param lists: a list of ListNode
#     @return: The head of one sorted list.
#     """
#     def mergeKLists(self, lists):
#         mid  = len(lists) // 2
#         return self.merge_sort(0, len(lists) - 1, lists)
        
#     """
#     分治算法一定有return
#     @param: start
#     @param: end
#     @return: merged head
#     """
#     def merge_sort(self, start, end, lists):
#         if start == end:
#             return lists[start]
        
#         mid = (start + end) // 2
#         left = self.merge_sort(start, mid, lists)
#         right = self.merge_sort(mid + 1, end, lists)
#         return self.merge(left, right)
        
#     def merge(self, left, right):
#         dummy = ListNode(0)
#         tail = dummy
#         while left and right:
#             if left.val < right.val:
#                 tail.next = left
#                 left = left.next
#             else:
#                 tail.next = right
#                 right = right.next
#             tail = tail.next
#         if left:
#             tail.next = left
#         if right:
#             tail.next = right
#         # while left:
#         #     tail.next = left
#         #     tail = left
#         #     left = left.next
#         # while right:
#         #     tail.next = right
#         #     tail = right
#         #     right = right.next
#         return dummy.next

"""
方法3，从下往上，2，2归并
2,2 合并O(N)
数的高度logK
所以O(Nlogk)
"""
from collections import deque
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        if not lists:
            return None
       
        current_list = lists
        
        while len(current_list) > 1:
            next_list = []
            index = 0
            for index in range(0, len(current_list), 2):
                if index + 1 < len(current_list):
                    next_list.append(self.merge(current_list[index], current_list[index + 1]))
                else:
                    next_list.append(current_list[index])
            current_list = next_list
        return current_list[0]
            
        
        
    def merge(self, left, right):
        dummy = ListNode(0)
        tail = dummy
        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        if left:
            tail.next = left
        if right:
            tail.next = right
        # while left:
        #     tail.next = left
        #     tail = left
        #     left = left.next
        # while right:
        #     tail.next = right
        #     tail = right
        #     right = right.next
        return dummy.next