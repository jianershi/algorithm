"""
装前i个物体，是否能完全占用j的空间。
f[i][j] 是一个boolean

"""
class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        # write your code here
        f = [[False] * (m + 1) for _ in range(len(A) + 1)]
        for i in range(len(A) + 1):
            for j in range(m + 1):
                if j == 0:
                    f[i][j] = True
                    continue
                if j - A[i - 1] < 0:
                    f[i][j] = f[i - 1][j]
                else:
                    f[i][j] = f[i - 1][j] or f[i - 1][j - A[i - 1]]
        for index in range(m, -1, -1):
            if f[len(A)][index] == True:
                return index
        return 0
        