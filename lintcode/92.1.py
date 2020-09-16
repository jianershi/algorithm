"""
92. Backpack
https://www.lintcode.com/problem/backpack/description?_from=ladder&&fromId=106
九章强化班

brute force: weather to take or not to take 2^n
dp:
for backpack, the maximum weight always is a dimention in DP.

dp[i][w]: weather i can use previous ith item into the bakcpack to make up weight w

wrong dp[i] definition: maximum weight i can put inside backpack without over capcity
ex. 3952 capacity 10
last step
395|2    3952
9        either to put last 2 or not. 2 over capacity don't put inside. 
total: 9.
best: 3+5+2 = 10.
why? because the requirement doesn't ask for maximum weight. 
instead, it asks for maximum weight with total capcity <= M.
-> it doesn't require previous iteration to be maximum

last step
dp[i][w] = dp[i - 1][w] or dp[i - 1][j - A[i - 1]] if w >= A[i - 1]
            ^ not using last object
                            ^ using last object

answer:
dp[n][j] for the last j in the sequence

initial condition:
dp[0][0] = True
dp[0][j] = False

"""
class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        # write your code here
        if not A:
            return False
        n = len(A)

        dp = [[False] * (m + 1) for _ in range(n + 1)]

        dp[0][0] = True #initial condition

        for i in range(1, n + 1):
            for j in range(m + 1): #m start from weight 0 to m, it represents weight
                dp[i][j] = dp[i - 1][j]
                if j >= A[i - 1]:
                    dp[i][j]  = dp[i][j] or dp[i - 1][j - A[i - 1]]

        return max([j for j, v in enumerate(dp[n]) if v == True]) #j -> is weight, don't need to -1