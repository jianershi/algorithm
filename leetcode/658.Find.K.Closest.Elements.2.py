"""
658. Find K Closest Elements
https://leetcode.com/problems/find-k-closest-elements/

thought:
using bisection search algorithm: 
1. finding the minimum difference to the target first
2. since the array is sorted, from that pivot, we only needs to look for left and right side using two pointers?

o(log(n) + k * 2 something like that

this is a bit cleaner.
it tries to find lower bound

"""
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        idx = self.findClosestIdxLessOrEqualToTarget(arr, x)
        print(idx)
        return self.findClosestK(arr, idx, k, x)
        
    def findClosestIdxLessOrEqualToTarget(self, arr, target):
        closest_idx = -1
        start, end = 0, len(arr) - 1
        
        while start < end:
            """
            since we are finding the lower bound, we have to avoid the situation where there might be a loop
            arr = [1,3], target = 2
                   ^ ^
                   s e
                   m<-(mid) if mid = (start + end) // 2 = 0
            arr[m] = 1 < 2, we are saying that it could be the mid(since we are doing lower bound), so s = mid(instead of mid + 1 which excludes mid from further search a.k.a. result)
            but, this results in search of [1,3] again
                                            ^ ^
                                            s e
                                            m
                                            which is a loop

            instead, we say m = (start + end + 1) // 2, so that m falls on the right side
            [1,3]
             s e
               m
            arr[m] > target(2), so e = m - 1
            [1,3]
             s
             e
             m
            end of search

            """
            mid = (start + end + 1) // 2
            if arr[mid] < target:
                start = mid
            elif arr[mid] > target:
                end = mid - 1
            else:
                return mid
        
        return start
    
    def findClosestK(self, arr, lowerBound, k, target):
        result = []
        count = 0
        if k == 0:
            return result
        """
        #since i am comapring two pointers, then i don't have to make sure the center is the smallest, i only have to find the first number that is less or more than the target. this makes the findClosestIdx logic easier and becomes findClosestIdxLessOrEqualToTarget
        """
        l, r = lowerBound, lowerBound + 1
        """
        notice i am using the lower bound, and lower bound + 1, reason being

        x  T  x
           ^ target
        ^lowerBound
              ^lowerBound + 1

        which makes sense.
        
        if instead, se compare lowerBound - 1, lowerBound
        then we will have 
        x x T y
          ^ lowerBound
        ^ lowerBound - 1
        there is no guarantee that y won't be closer to T compared to either lowerBound - 1 or lowerBound

        in order to user lowerBound, lowerBound - 1, we actually have to find uppwerBound - 1, uppwerBound
        x T x
            ^ uppwerBound
        ^ upperBound - 1

        """
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