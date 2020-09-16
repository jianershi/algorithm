"""
125. Backpack II
https://www.lintcode.com/problem/backpack-ii/description


still has 1 dimention as capacity.
dp[w]

dp? max value i can make for putting previous ith item with weight w into the backpack
last step:
to put or not to put
dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - A[i - 1]] + V[i - 1])
dp2[i][w] weather i use prev ith item to make them weigh w,
here, because value cannot be negative, i can save this by checking dp[i - 1][w - A[i - 1]] is -1 or not
vise versa, even if dp[i - 1][w] is negative, it is going to choose dp[i - 1][w - A[i - 1]] + V[i - 1] because it will be larger

initial condition:
dp[0][0] = 0 # previous 0 item can make upto make up to weight 0 and they have max value of 0
dp[0][1..m] = -1 #impossible

answer:
max(dp[n])

sliding array

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
        if not A or not V:
            return 0
        n = len(A)

        dp = [[0] * (m + 1) for _ in range(2)]

        old, now = 0, 0

        for j in range(1, m + 1):
            dp[now][j] = -1

        for i in range(1, n + 1):
            old = now
            now = 1 - now
            for j in range(m + 1):
                dp[now][j] = dp[old][j]
                if j >= A[i - 1] and dp[old][j - A[i - 1]] != - 1:
                    dp[now][j] = max(dp[now][j], dp[old][j - A[i - 1]] + V[i - 1])

        return max(dp[now])
