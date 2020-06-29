"""
34. N-Queens II
https://www.lintcode.com/problem/n-queens-ii/description
"""
class Result:
    def __init__(self):
        self.count = 0
        
class Solution:
    """
    @param n: The number of queens.
    @return: The total number of distinct solutions.
    """
    def totalNQueens(self, n):
        # write your code here

        result = Result()
        visited_col = [0] * n #0 - n-1
        visited_sum = [0] * (2 * n - 1)  #0 - 2n - 2
        visited_diff = [0] * (2 * n - 1)  # - n + 1 -- n - 1
        self.dfs(n, [], result, visited_col, visited_sum, visited_diff)
        return result.count

    def dfs(self, n, cols, result, visited_col, visited_sum, visited_diff):
        row = len(cols)
        if row == n:
            result.count += 1
            return

        for j in range(n):
            if not self.is_valid(n, row, j, cols, visited_col, visited_sum, visited_diff):
                continue
            cols.append(j)
            visited_col[j] = 1
            visited_sum[row + j] = 1
            visited_diff[row - j + n - 1] = 1
            self.dfs(n, cols, result, visited_col, visited_sum, visited_diff)
            visited_col[j] = 0
            visited_sum[row + j] = 0
            visited_diff[row - j + n - 1] = 0
            cols.pop()

    def is_valid(self, n, row, col, cols, visited_col, visited_sum, visited_diff):
        return visited_col[col] + visited_sum[row + col] + visited_diff[row - col + n - 1] == 0
