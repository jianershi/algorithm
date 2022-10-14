"""
658. Find K Closest Elements
https://leetcode.com/problems/find-k-closest-elements/

thought:
using bisection search algorithm: 
1. finding the minimum difference to the target first
2. since the array is sorted, from that pivot, we only needs to look for left and right side using two pointers?

o(log(n) + k * 2 something like that

really bad solution. 

"""
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        center = self.findClosestIdx(arr, x)
        print(center)
        return self.findClosestK(arr, center, k, x)
        
    def findClosestIdx(self, arr, target):
        min_diff = sys.maxsize
        closest_idx = -1
        start, end = 0, len(arr) - 1
        
        while start < end:
            mid = (start + end) // 2
            if arr[mid] < target:
                start = mid + 1
                if abs(arr[mid] - target) < min_diff:
                    closest_idx = mid
                    min_diff = abs(arr[mid] - target) 
            elif arr[mid] > target:
                end = mid - 1
                if abs(arr[mid] - target) < min_diff:
                    closest_idx = mid
                    min_diff = abs(arr[mid] - target) 
            else:
                return mid
        
        if abs(arr[start] - target) <= min_diff:
            min_diff = abs(arr[start] - target)
        if abs(arr[end] - target) <= min_diff:
            min_diff = abs(arr[end] - target)
        for idx in sorted([closest_idx, start, end]):
            if abs(arr[idx] - target) <= min_diff: 
                print(idx, arr[idx])
                return idx
        
        return -1
    
    def findClosestK(self, arr, center, k, target):
        result = []
        count = 0
        if k == 0:
            return result
        l, r = center, center + 1
        while 0 <= l and l <= r and r < len(arr) and count < k:
            if abs(arr[l] - target) <= abs(arr[r] - target):
                result.append(arr[l])
                count += 1
                l -= 1
            else:
                result.append(arr[r])
                count += 1
                r += 1
        """
        attach the rest of the array in oppotite direction if one pointer reaches the border
        ..................
            ^l           ^r
                          ^r
         ^^^^l <- attach from left pointer leftwards only

         same logic if left pointer reaches the 0,
         then only have to attach right pointer rightwards                 
        """
        if l < 0:
            while r < len(arr) and count < k:
                result.append(arr[r])
                count += 1
                r += 1
                
        if r >= len(arr):
            while l >= 0 and count < k:
                result.append(arr[l])
                count += 1
                l -= 1
        
                
        return sorted(result)