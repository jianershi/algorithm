"""
798. Backpack VII
https://www.lintcode.com/problem/backpack-vii/description

Input:  n = 8, prices = [3,2], weights = [300,160], amounts = [1,6]
Output:  640
Explanation:  Buy the second rice(price = 2) use all 8 money.

n = 8 ->capacity
prices -> weight
weights -> value
amount:
processed_prices
processed_weight
m: type of goods

dp[i][j] = considering previous ith item, with it fill exactly j weight's max prices.

dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - processed_prices[i]] + processed_weight[i])

initil condition:
dp[i][0] = 0

answer:
max(dp[len(processed_prices)])

calculation direction: i 0 -> len(processed_prices), j 0 -> n

2D Sliding Array Optimization

"""
class Solution:
    """
    @param n: the money of you
    @param prices: the price of rice[i]
    @param weight: the weight of rice[i]
    @param amounts: the amount of rice[i]
    @return: the maximum weight
    """
    def backPackVII(self, n, prices, weight, amounts):
        # write your code here
        m = len(prices)
        processed_weight, processed_prices = [], []

        for i in range(m):
            for j in range(amounts[i]):
                processed_weight.append(weight[i])
                processed_prices.append(prices[i])

        dp = [[0] * (n + 1) for _ in range(2)]

        new, old = 0, 0

        for i in range(1, len(processed_prices) + 1):
            old = new
            new = 1 - new
            for j in range(1, n + 1):
                dp[new][j] = dp[old][j]
                if j >= processed_prices[i - 1]:
                    dp[new][j] = max(dp[new][j], dp[old][j - processed_prices[i - 1]] + processed_weight[i - 1])

        return max(dp[new])

