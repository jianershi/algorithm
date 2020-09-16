"""
1861. Rat Jump
https://www.lintcode.com/problem/rat-jump/description?_from=ladder&&fromId=160
九章高频题班 google

odd_steps = [1, 3, 4]
even_steps = [1, 2, 4]

dp[i][even/odd] : number of ways to jump to position i and even/odd step next

dp[i + even_steps[j]][DataType.ODD] += dp[i][DataType.EVEN] for j in range(3)
dp[i + odd_steps[j]][DataType.EVEN] += dp[i][DataType.ODD] for j in range(3)

if i + enve_steps[j] > n - 1 (past 0), count everything into last step n - 1

initial condition
dp[0][DataType.ODD] = 1

answer

dp[n - 1][ODD] + dp[n - 1][EVEN]
"""
class DataType:
    ODD = 1
    EVEN = 0

class Solution:
    """
    @param arr: the steps whether have glue
    @return: the sum of the answers
    """
    def ratJump(self, arr):
        # Write your code here.
        MOD = int(1e9 + 7)
        if not arr:
            return 0
        n = len(arr)
        odd_steps = [1, 2, 4]
        even_steps = [1, 3, 4]
        

        dp = [[0] * 2 for _ in range(n)]

        dp[0][DataType.ODD] = 1

        for i in range(n - 1): #n = 3, 0, 1, 2, at n - 1, it is already at ground, so cannot jump, so last number is n -2
            for j in range(3):
                if i + even_steps[j] > n - 1 or arr[i + even_steps[j]] == 0:
                    dp[min(i + even_steps[j], n - 1)][DataType.ODD] += dp[i][DataType.EVEN] % MOD
                if i + odd_steps[j] > n - 1 or arr[i + odd_steps[j]] == 0:
                    dp[min(i + odd_steps[j], n - 1)][DataType.EVEN] += dp[i][DataType.ODD] % MOD

        return sum(dp[n - 1]) % MOD