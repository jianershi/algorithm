"""
1049. Last Stone Weight II
https://leetcode.com/problems/last-stone-weight-ii/

dp[i][j]: whether i can reach j weight from previosu i items

dp[i][0] = True , any previous item can make up weight 0


answer:
dp[i][j] last j so that dp is true

-> find a maximum value of weight j so that j <= target = total_sum / 2.0

suppose stones are divided into two piles of minimal sum difference.

pile_a = [a0, a1, a2]
pile_b = [b0, b1, b2]

then when they combine, sum(pile_a) - sum(pile_b) = smallest_possible_weight

[2,7,4,1,8,1] - >
pile_a = [2 8 1] = 11
pile_b = [4 7 1] = 12
4-2 = 2
pile_a = [8 1]
pile_b = [2 7 1]
8-7 = 1
pile_a = [1 1]
pile_b = [2 1]
2-1 = 1
pile_a = [1]
pile_b = [1 1]
1-1 = 1
pile_a = []
pile_b = [1]

"""
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_sum = sum(stones)
        target = total_sum // 2 #use lower bound
        n = len(stones)

        dp = [[False] * (target + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = True
            for j in range(1, target + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= stones[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j - stones[i - 1]]
        
        for j in range(target, -1, -1):
            if dp[n][j] == True:
                return total_sum - j - j
