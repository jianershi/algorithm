"""
658. Find K Closest Elements
https://leetcode.com/problems/find-k-closest-elements/

thought:
using bisection search algorithm: 
1. finding the minimum difference to the target first
2. since the array is sorted, from that pivot, we only needs to look for left and right side using two pointers?

o(log(n) + k * 2 something like that

this is a bit cleaner.
it tries to find upper bound. 

*** same method as `658.Find.K.Closest.Elements.2.py` but using upper bound instead ***

"""
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        idx = self.findClosestIdxLargerOrEqualToTarget(arr, x)
        print(idx)
        return self.findClosestK(arr, idx, k, x)
        
    def findClosestIdxLargerOrEqualToTarget(self, arr, target):
        closest_idx = -1
        start, end = 0, len(arr) - 1
        
        while start < end:
            mid = (start + end) // 2
            if arr[mid] > target:
                end = mid
            elif arr[mid] < target:
                start = mid + 1
            else:
                return mid
        
        return end
    
    def findClosestK(self, arr, upperBound, k, target):
        result = []
        count = 0
        if k == 0:
            return result
        l, r = upperBound - 1, upperBound
        for _ in range(k):
            if self.isLeftCloser(arr, l, r, target):
                result.append(arr[l])
                l -= 1
            else:
                result.append(arr[r])
                r += 1
                
        return sorted(result)
    
    def isLeftCloser(self, arr, left, right, target):
        if left < 0:
            return False
        if right >= len(arr):
            return True
        return abs(arr[left] - target) <= abs(arr[right] - target)