"""
因为存在方向性并且求最值。所以可以用dp
f[i][j] is the minimum sum to point i, j
f[i][j] = min(f[i - 1][j], f[i][j - 1]) + X[i][j]
initalization
f[0][0] = X[i][j]
然后看左边和最上面是否要单独考虑
不需要。
计算顺序left -> right top->bottom
answer:
f[m - 1][n - 1]


继续优化使用分开策略
f[i][j] += X[i][j]
if i > 0:
    f[i][j] += f[i - 1][j]
if j > 0:

"""
# class Solution:
#     """
#     @param grid: a list of lists of integers
#     @return: An integer, minimizes the sum of all numbers along its path
#     """
#     def minPathSum(self, grid):
#         # write your code here
#         m = len(grid)
#         n = len(grid[0])

#         f = [[0] * n for _ in range(m)]

#         for i in range(m):
#             for j in range(n):
#                 f[i][j] = grid[i][j]
#                 if i == 0 and j == 0:
#                     continue
#                 if i == 0:
#                     f[i][j] += f[i][j - 1]
#                     continue
#                 if j == 0:
#                     f[i][j] += f[i - 1][j]
#                     continue
#                 f[i][j] += min(f[i - 1][j], f[i][j - 1])
#         return f[m - 1][n - 1]
"""
滚动数组
"""
class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        # write your code here
        m = len(grid)
        n = len(grid[0])

        f = [[0] * n for _ in range(2)]

        for i in range(m):
            for j in range(n):
                f[i % 2][j] = grid[i][j]
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    f[i % 2][j] += f[i % 2][j - 1]
                    continue
                if j == 0:
                    f[i % 2][j] += f[(i - 1) % 2][j]
                    continue
                f[i % 2][j] += min(f[(i - 1) % 2][j], f[i % 2][j - 1])
        return f[(m - 1) % 2][n - 1]
"""
同样可以用一个数组解决
"""
# class Solution:
#     """
#     @param grid: a list of lists of integers
#     @return: An integer, minimizes the sum of all numbers along its path
#     """
#     def minPathSum(self, grid):
#         if not grid or not grid[0]:
#             return 0
#         m = len(grid)
#         n = len(grid[0])

#         f = [0] * n
#         f[0] = grid[0][0]

#         for i in range(m):
#             for j in range(n):
#                 if i > 0 and j > 0:
#                     f[j] = min(f[j], f[j - 1])
#                     f[j] += grid[i][j]
#                     continue
#                 if i > 0:
#                     f[j] += grid[i][j]
#                     continue
#                 if j > 0:
#                     f[j] += f[j - 1] + grid[i][j]
#                     continue
#         return f[n - 1]
                
