"""
162. Find Peak Element
https://leetcode.com/problems/find-peak-element/
different method

using divide an conquer

http://courses.csail.mit.edu/6.006/spring11/lectures/lec02.pdf
"""

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        return self.findPeak1D(nums, start, end)    
        
    def findPeak1D(self, nums, start, end):
        mid = (start + end) // 2
        if self.isBigger(nums, mid, mid - 1) and self.isBigger(nums, mid, mid + 1):
            return mid
        elif self.isBigger(nums, mid - 1, mid):
            return self.findPeak1D(nums, start, mid - 1)
        elif self.isBigger(nums, mid + 1, mid):
            return self.findPeak1D(nums, mid + 1, end)
        else:
            return [-1, -1]
    
    def isBigger(self, nums, bigger, smaller):
        n = len(nums)
        bigger_number, smaller_number = -sys.maxsize, -sys.maxsize
        if 0 <= bigger < n:
            bigger_number = nums[bigger]
        if 0 <= smaller < n:
            smaller_number = nums[smaller]
        return bigger_number > smaller_number