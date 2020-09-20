"""
1594. Maximum Non Negative Product in a Matrix
https://leetcode.com/contest/weekly-contest-207/problems/maximum-non-negative-product-in-a-matrix/
TLE
"""
DIRECTIONS = [
    (0, 1),
    (1, 0)
]
class Solution:
    def __init__(self):
        self.max_product = -1

    def maxProductPath(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        self.dfs(0, 0, grid, set(), grid[0][0], {})
        return self.max_product % 1000000007 if self.max_product >= 0 else -1

    def dfs(self, x, y, grid, visited, product, memo):
        n = len(grid)
        m = len(grid[0])

        if (x, y) == (n - 1, m - 1):
            self.max_product = max(self.max_product, product)
            return

        for dx, dy in DIRECTIONS:
            nx = x + dx
            ny = y + dy
            if (nx, ny) in visited:
                continue
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            visited.add((nx,ny))
            self.dfs(nx, ny, grid, visited, product * grid[nx][ny], memo)
            visited.remove((nx,ny))

