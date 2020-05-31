"""
parition dp
f[k][i]: minimum time it will take for the first k copier to copy first i books
funciton:
f[k][i] = min for j=0..i(max(f[k - 1][j], A[j] + ... + A[i - 1]))
intial:
f[0][0] = 0
f[0][x] = sys.maxsize
f[k][0] = 0
answer:f[k][n - 1]
"""
# import sys
# class Solution:
#     """
#     @param pages: an array of integers
#     @param k: An integer
#     @return: an integer
#     """
#     def copyBooks(self, pages, K):
#         # write your code here
#         if not pages:
#             return 0
#         f = [[sys.maxsize] * len(pages) for _ in range(K + 1)]
#         for i in range(len(pages)):
#             f[0][i] = sys.maxsize
#         for k in range(K + 1):
#             f[k][0] = 0
#
#         for k in range(K + 1):
#             for i in range(len(pages)):
#                 sum = 0
#                 for j in range(0, i + 1):
#                     f[k][i] = min(f[k][i], max(f[k - 1][j], sum))
#
