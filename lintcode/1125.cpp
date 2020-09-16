/**
 * 1125. Jump Pillar
 * https://www.lintcode.com/problem/jump-pillar/description
 * DP
 * dp[i][j] : whether can reach index i with j remaining chance
 *
 * not using super power
 * dp[i][1] = dp[i - x][1] for 1 <= x <= k and dp[i] <= dp[i - k]
 * 
 * if 0 super power chance left, either use super power at this step or have already used it in the past.
 * dp[i][0] = dp[i - x][1] | (dp[i - x][0] dp[i] <= dp[i - k]) for 1 <= x <= k
 *
 * answer:
 * dp[n - 1][0] || dp [n - 1][1]
 *
 * intial conditon:
 * dp[0][0] = true;
 * dp[0][1] = true;
 * regardless of using super power or not, one can always reach the first position.
 */

/**
 * dp[i][j] : whether can reach prev ith position with j remaining chance
 * dp[i][1] = dp[i - x][0] for 1 <= x <= k and dp[i - x] >= dp[i]
 * dp[i][0] = dp[i - x][1] | dp[i - x][0] for 1 <= x <= k
 * 
 * initial dp[0][0] = true;
 */ 
class Solution {
public:
    /**
     * @param h: the height of n pillar
     * @param k: the limit
     * @return: Xiao Yi can or can't reach the n-th pillar
     */
    bool jumpPillar(vector<int> &h, int k) {
        // write your code here.
        int n = h.size();
        bool dp[n][2];
        memset(dp, false, sizeof dp);
        dp[0][0] = true;
        dp[0][1] = true;
        for (int i = 1; i < n; ++i) {
            for (int x = 1; x <= k && i - x >= 0; ++x) {
                dp[i][0] = dp[i][0] || dp[i - x][1];
                if (h[i - x] >= h[i]) {
                    dp[i][0] = dp[i][0] || dp[i - x][0];
                    dp[i][1] = dp[i][1] || dp[i - x][1];
                }
            }
        }
        return dp[n - 1][0] || dp[n - 1][1];
    }
};