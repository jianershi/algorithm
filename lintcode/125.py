"""
背包问题
确定状态：f[i][j]代表取前面i个物体，占用j空间所取得的最大价值
转移方程：f[i][j] = max(f[i - 1][j], f[[i - 1][j - A[i]] + V[i])
初始条件：
f[0][j] = 0
f[i][0] = 0
边界条件
j - A[i] >= 0
为了不特殊处理第一行和第一列。
插入一行0，插入一行列。

答案：
f[len(A)][m]
计算顺序：
从左往右

"""
class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """
    def backPackII(self, m, A, V):
        # write your code here
        f = [[0] * (m + 1) for _ in range(len(A) +  1)]
        for i in range(len(A) + 1):
            for j in range(m + 1):
                if i == 0 or j == 0:
                    continue
                if j-A[i - 1] < 0:
                    f[i][j] = f[i - 1][j]
                else:
                    f[i][j] = max(f[i - 1][j], f[i - 1][j - A[i - 1]] + V[i - 1])
        return f[len(A)][m]