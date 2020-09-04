/**
 * 983. Minimum Cost For Tickets
 * https://leetcode.com/problems/minimum-cost-for-tickets/
 * dp
 */
class Solution {
public:
    int mincostTickets(vector<int>& days, vector<int>& costs) {
        int n = *max_element(days.begin(), days.end());
        unordered_set<int> travel(days.begin(), days.end());
        int dp[n+1];
        memset(dp, 0, sizeof dp);
        for (int i = 1; i < n + 1; ++i) {
            if (travel.find(i) == travel.end()) {
                dp[i] = dp[i - 1];
                continue;
            }
            dp[i] = min({
                dp[i - 1] + costs[0], 
                dp[max(0, i - 7)] + costs[1], 
                dp[max(0, i - 30)] + costs[2]
            });
        }
        return dp[n];
    }
};