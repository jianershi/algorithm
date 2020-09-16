"""
440. Backpack III
https://www.lintcode.com/problem/backpack-iii/description
九章强化班

infinite number of items

still have capcity m: so need to have 1d in dp for weight

dp as value of the 
dp[i][w]: max value for putting previous k * ith kind of item into the backpack that makes up to total weight w

last step
dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - k * A[i - 1]] + k * V[i - 1]) for all k combinations
         = max(dp[i - 1][w - k * A[i - 1]] + k * V[i - 1]) for all k, w - k * A[i - 1] >= 0 ==> k <= w/ A[i - 1] ==> k <= m / 1 == > k <= m

time complexity:
o(n * m * m)
  ^ type of item
      ^ weight
          ^ for iterate through k


optimization
dp[i][w] = max(dp[i - 1][w], dp[i][w - A[i - 1]] + V[i - 1]) #see lecture note

answer:
max(dp[n][w]), don't care about weight, only care about max values

initial condition:
dp[0][0] = 0
dp[0][j] = -1

sliding array optimization

"""
class Solution:
    """
    @param A: an integer array
    @param V: an integer array
    @param m: An integer
    @return: an array
    """
    def backPackIII(self, A, V, m):
        # write your code here
        if not A or not V:
            return 0

        n = len(A)
        if len(V) != n:
            return 0

        dp = [[0] * (m + 1) for _ in range(2)]
        old, now = 0, 0

        for j in range(1, m + 1):
            dp[now][j] = -1
            
        for i in range(1, n + 1):
            old = now
            now = 1 - now
                
            for j in range(m + 1):
                dp[now][j] = dp[old][j]
                if j >= A[i - 1] and dp[now][j - A[i - 1]] != -1:
                    dp[now][j] = max(dp[now][j], dp[now][j - A[i - 1]] + V[i - 1])

        return max(dp[now])