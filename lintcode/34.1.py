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
        visited = {
            "col": set(),
            "sum": set(),
            "diff": set(),
        }
        self.dfs(n, [], result, visited)
        return result.count

    def dfs(self, n, cols, result, visited):
        row = len(cols)
        if row == n:
            result.count += 1
            return

        for j in range(n):
            if not self.is_valid(row, j, cols, visited):
                continue
            cols.append(j)
            visited["col"].add(j)
            visited["sum"].add(row + j)
            visited["diff"].add(row - j)
            self.dfs(n, cols, result, visited)
            visited["col"].remove(j)
            visited["sum"].remove(row + j)
            visited["diff"].remove(row - j)
            cols.pop()

    def is_valid(self, row, col, cols, visited):
        if col in visited["col"] or row + col in visited["sum"] or row - col in visited["diff"]: 
            return False
        return True

