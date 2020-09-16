/**
10. Regular Expression Matching
https://leetcode.com/problems/regular-expression-matching/
https://leetcode.com/problems/regular-expression-matching/discuss/5651/Easy-DP-Java-Solution-with-detailed-Explanation
**/
class Solution {
public:
    bool isMatch(string s, string p) {
        int n = s.size(), m = p.size();
        bool dp[n + 1][m + 1];
        memset(dp, false, sizeof dp);
        dp[0][0] = true;
        for (int j = 2; j < m + 1; ++j) {
            dp[0][j] = p[j - 1] == '*' && dp[0][j - 2];
        }
        for (int i = 1; i < n + 1; ++i) {
            for (int j = 1; j < m + 1; ++j) {
                if (s[i - 1] == p[j - 1] || p[j - 1] == '.') {
                    dp[i][j] = dp[i - 1][j - 1];
                } else if (p[j - 1] == '*') {
                    if (p[j - 2] != '.' && p[j - 2] != s[i - 1]) {
                        dp[i][j] = dp[i][j - 2];
                    } else {
                        dp[i][j] = dp[i][j - 2] || dp[i - 1][j - 2] || dp[i - 1][j];
                    }
                }
            }
        }
        return dp[n][m];
    }
};
