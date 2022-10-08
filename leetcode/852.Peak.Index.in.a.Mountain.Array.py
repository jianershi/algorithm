"""
585. Maximum Number in Mountain Sequence

852. Peak Index in a Mountain Array
https://leetcode.com/problems/peak-index-in-a-mountain-array/

"""
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start, end = 0, len(arr) - 1
        while start < end:
            mid = (start + end) // 2
            """
            mid + 1 will never be out of range, because start < end guarantee the last time it will run is between adjacent indexes, such as [start=0, end=1], then it also guaranteed by (start + end) // 2 which always falls on the left side in this case, thus mid + 1 will be 0 + 1 = 1 = end, which will not be out of range
            """
            if arr[mid] < arr[mid + 1]: 
                start = mid + 1
                """
                when current element is strictly smaller than next element, then we know for sure that the top is on the right, not on mid, but at least on mid + 1
                """
            else:
                """
                1) when current element is equals to the element on the right, not possible, by definition, each element is different
                2) when current element is larger than the lemenet on the right, then, we know that it is on the left, including the current element, because there is no guarantee that there exist a number such that num[i] > num[mid], the largest number could be the mid, so we use end = mid instead of end = mid - 1
                """
                end = mid
            
        return start