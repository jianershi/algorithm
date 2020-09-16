/**
 * 338. Paint House III
 * https://www.lintcode.com/problem/paint-house-iii/leaderboard
 * 周赛
 * 
 * dp[i][j][0]: minimum cost for previous ith houses to be colored to color j with 0 super power left.
 * dp[i][j][1]: minimum cost for previous ith houses to be colored to color j with 1 super power left.
 *
 * similar to problem 
 * 1125. Jump Pillar
 * https://www.lintcode.com/problem/jump-pillar/description
 * 
 * dp[i][j][1] = min(dp[i - 1][k][1] * costs[i - 1][j][1] for k (all color except j))
 * 
 * dp[i][j][0] = 1) min(dp[i - 1][k][0] * costs[i - 1][j][0] for k (all color except j))                    <- 0 super power left, choose not to use it this time
 *            or 2) min(dp[i - p + 1][1] + cost of painting all the house from i - p to current same color) <- 0 super power left, choose to use it this time.
 * 
 * 
 */
class Solution {
public:
    /**
     * @param costs: costs of paint ith house into color j
     * @param t: maximum length of street
     * @return: minimum costs of painting all houses
     */
    int paintHouseIII(vector<vector<int>> &costs, int t) {
        // Write your code here.
        int n = costs.size();
        int m = costs[0].size();
        int dp[n+1][m][2];
        // for (int i = 0; i < n + 1; ++i)
        //     for (int j = 0; j < m; ++j)
        //         for (int x = 0; x < 2; ++x)
        //             dp[i][j][x] = INT_MAX;
        memset(dp, 0x3f, sizeof dp); //~equivalent to the 4 lines above
        
        for (int j = 0; j < m; ++j) {
            dp[0][j][0] = 0;
            dp[0][j][1] = 0;
        }
        
        //prefix sum to calculate every house to be painted the same color
        //prefix_sum[i][j]: total cost for previous ith houses to be painted to j color
        vector<vector<int>> prefix_sum(n+1, vector<int>(m, 0));
        for (int j = 0; j < m; ++j) {
            for (int i = 1; i < n + 1; ++i) {
                prefix_sum[i][j] = prefix_sum[i - 1][j] + costs[i - 1][j];
            }
        }
        
        for (int i = 1; i < n + 1; ++i) {
            for (int j = 0; j < m; ++j) {
                for (int k = 0; k < m; ++k) {
                    if (k == j) continue;
                    dp[i][j][1] = min(dp[i][j][1], dp[i - 1][k][1] + costs[i - 1][j]);
                    dp[i][j][0] = min(dp[i][j][0], dp[i - 1][k][0] + costs[i - 1][j]);
                }
                for (int p = 2; p <= t; ++p) {
                    if (i - p + 1 >=0)
                        dp[i][j][0] = min(dp[i][j][0], dp[i - p + 1][j][1] + prefix_sum[i][j] - prefix_sum[i - p + 1][j]);
                }
            }
        }
        
        int min_cost = INT_MAX;
        for (int j = 0; j < m; ++j) {
            min_cost = min({min_cost, dp[n][j][1], dp[n][j][0]});
        }
        
        return min_cost;
    }
};