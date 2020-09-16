/**
 * 515. Paint House
 * https://www.lintcode.com/problem/paint-house/description
 * 256. Paint House
 * https://leetcode.com/problems/paint-house/
 */
class Solution {
public:
    /**
     * @param costs: n x 3 cost matrix
     * @return: An integer, the minimum cost to paint all houses
     */
    int minCost(vector<vector<int>> &costs) {
        // write your code here
        int n = costs.size();
        int dp[n + 1][3];
        memset(dp, 0, sizeof dp);
        
        for (int i = 1; i < n + 1; ++i) {
            dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + costs[i - 1][0];
            dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i - 1][1];
            dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + costs[i - 1][2];
        }
        return min({dp[n][0], dp[n][1], dp[n][2]});
    }
};