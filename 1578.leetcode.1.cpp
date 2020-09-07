/**
 * 1578. Minimum Deletion Cost to Avoid Repeating Letters
 * https://leetcode.com/problems/minimum-deletion-cost-to-avoid-repeating-letters/
 *
 * dp[i][j]: previous ith digit(in the original sequence) matches the condition with last digit = j
 *
 * similar to edit disntace
 */
class Solution {
public:
    int minCost(string s, vector<int>& cost) {
        int n = s.size();
        vector<vector<int>> dp(n + 1, vector<int>(26, 0));
        for (int i = 1; i < n + 1; ++i) {
            int curr = s[i - 1] - 'a';
            //delete current char: then ith digit becomes i - 1th digit. 
            //  abdd i = 3
            //     ^
            //  abd 2
            //  this step is edit distance 
            for (int j = 0; j < 26; ++j) {
                dp[i][j] = dp[i - 1][j] + cost[i - 1];
            }
            //keep current char, choose other chars for prev position
            for (int j = 0; j < 26; ++j){
                if (curr == j) continue;
                dp[i][curr] = min(dp[i][curr], dp[i - 1][j]);
            } 
        }
        return *min_element(dp[n].begin(), dp[n].end());
    }
};