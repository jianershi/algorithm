"""
1853. Efficient Job Processing Service
https://www.lintcode.com/problem/efficient-job-processing-service/description?_from=ladder&&fromId=160

p: max run time -> capacity
weights: weights of every task
tasks: duration of each task
? : max total weight can be processed

knapsack problem?

dp[i][j]: max total weight that can be processed with previous i tasks that reaches time of j
dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - tasks[i - 1]] + weights[i - 1])

initial condition
dp[0][0] = 0 considering previosu 0 tasks, to reach time of 0, will have max weight of 0

answer:
dp[n][p]

"""
class Solution:
    """
    @param n: the number of tasks
    @param weights: the weight for every task
    @param tasks: the actual duration of every task
    @param p: maximum runtime for Pigeon in an hour
    @return: the maximum total weight that the Pigeon service can achieve in an hour
    """
    def maxWeight(self, n, weights, tasks, p):
        # write your code here
        n = len(tasks)
        dp = [[0] * (p // 2 + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, p // 2 + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= tasks[i - 1]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - tasks[i - 1]] + weights[i - 1])

        return dp[n][p // 2]