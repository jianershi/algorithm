"""
510. Maximal Rectangle
https://www.lintcode.com/problem/maximal-rectangle/description
Input:
[
  [1, 1, 0, 0, 1],
  [0, 1, 0, 0, 1],
  [0, 0, 1, 1, 1],
  [0, 0, 1, 1, 1],
  [0, 0, 0, 0, 1]
]
Output: 6
same problem as 122. Largest Rectangle in Histogram. apply monotonous stack to each row.

"""
class Solution:
    """
    @param matrix: a boolean 2D matrix
    @return: an integer
    """
    def maximalRectangle(self, matrix):
        # write your code here
        max_area = 0
        if not matrix or not matrix[0]:
            return max_area

        n = len(matrix)
        m = len(matrix[0])

        curr_level_height = [0] * m
        for i in range(n):
            stack = []
            for j in range(m + 1):
                if j == m:
                    curr_height = -1
                elif matrix[i][j] == 0:
                    curr_height = 0
                    curr_level_height[j] = 0
                else:
                    curr_height = curr_level_height[j] + 1
                    curr_level_height[j] = curr_height
                while stack and curr_height <= curr_level_height[stack[-1]]:
                    h = curr_level_height[stack.pop()]
                    l = 0 if len(stack) == 0 else stack[-1] + 1
                    r = j - 1
                    area = (r - l + 1) * h
                    max_area = max(max_area, area)

                stack.append(j)
        return max_area
