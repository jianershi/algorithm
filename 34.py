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
        self.dfs(n, [], result)
        return result.count

    def dfs(self, n, cols, result):
        row = len(cols)
        if row == n:
            result.count += 1
            return

        for j in range(n):
            if not self.is_valid(row, j, cols):
                continue
            cols.append(j)
            self.dfs(n, cols, result)
            cols.pop()

    def is_valid(self, row, col, cols):
        for r,c in enumerate(cols):
            if col == c:
                return False
            if r + c == row + col:
                return False
            if r - c  == row - col:
                return False
        return True

