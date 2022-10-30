"""
1901. Find a Peak Element II
https://leetcode.com/problems/find-a-peak-element-ii/

m x n matrix
time complexity o(m * logn)

1. finding global maximum inside the mid col g = max(col[i])
2. if the maximum element inside this col (g) is a 2d peak, then by definition it is a 2d peak, return
3. if not, that means the neighboring col has an element larger than it
4. but since g is the largest element of this col, if the neighboring element is larger than this number, it means there exists a larger number in the neighboring col that is going to be larger than *every number* in this col <- by definition, that is where peaks are heading
5. we can safely discard the search
"""
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        return self.bisection(mat, 0, n - 1)
                            
    def bisection(self, mat, start, end):
        while start < end:
            mid = (start + end) // 2
            m, n = len(mat), len(mat[0])
            #find max number in center col
            max_number_row_idx = self.maxIdxInACol(mat, mid)
            if mat[max_number_row_idx][mid + 1] > mat[max_number_row_idx][mid]:
                start = mid + 1
            else:
                end = mid
        #because the bisection method will only stop at the right col, but within that col,
        #max row need to be calcualted again
        return [self.maxIdxInACol(mat, start), start]
        
    def maxIdxInACol(self, mat, col):
        #find max number in center col
        max_number_row_idx, max_number = -1, -1
        for i in range(0, len(mat)):
            if mat[i][col] > max_number:
                max_number = mat[i][col]
                max_number_row_idx = i
        return max_number_row_idx