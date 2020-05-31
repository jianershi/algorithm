class Solution:
    """
    @param boxes: number of pens for each box
    @param target: the target number
    @return: the minimum boxes
    """
    def minimumBoxes(self, boxes, target):
        # write your code here


    """
    return -1 if not exist
    """
    def min_length_subarray(self, boxes, target):
        if not boxes:
            return -1
        left = 0
        right = 0
        min_subarray_sum = 0
        min_left = [sys.maxsize] * len(boxes)
        subarray_sum = boxes[left]
        while right < len(boxes) - 1:
            #if left == right:
            if left != right:
                subarray_sum += boxes[right]
                while subarray_sum > target:
                    left += 1
                if subarray_sum != target:
                    min_left[right] = min_left[right - 1]
                if subarray_sum == target:
                    min_left[right] = min(min_left[right - 1], right - left + 1)
            
