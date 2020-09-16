"""
1833. pen box

https://www.lintcode.com/problem/pen-box/description
"""

class Solution:
    """
    @param boxes: number of pens for each box
    @param target: the target number
    @return: the minimum boxes
    """
    def minimumBoxes(self, boxes, target):
        # write your code here
        n = len(boxes)
        min_length = sys.maxsize
        min_left = self.min_length_subarray(boxes, target)
        min_right = self.min_length_subarray(boxes[::-1], target)[::-1]
        for i in range(n - 1):
            min_length = min(min_length, min_left[i] + min_right[i + 1])
        return min_length if min_length != sys.maxsize else -1

    """
    return -1 if not exist
    """
    def min_length_subarray(self, boxes, target):
        if not boxes:
            return sys.maxsize
        left = 0
        right = 0
        subarray_sum = 0
        min_left = [sys.maxsize] * len(boxes)
        while right < len(boxes):
            subarray_sum += boxes[right]
            while subarray_sum > target:
                subarray_sum -= boxes[left]
                left += 1
            # if right == 0 and subarray_sum == target:
            #     min_left[right] = 1
            if subarray_sum != target:
                min_left[right] = min_left[right - 1]
            if subarray_sum == target:
                min_left[right] = min(min_left[right - 1], right - left + 1)
            right += 1
        return min_left
