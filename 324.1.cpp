/**
324. Regular Expression Search
https://www.lintcode.com/problem/regular-expression-search/description
solution based on DP solution of leetcode 10:
https://leetcode.com/problems/regular-expression-matching/
https://leetcode.com/problems/regular-expression-matching/discuss/5651/Easy-DP-Java-Solution-with-detailed-Explanation

2d array 说实话这个优化很恶心。。不明不白的。可读性变差很多。
**/
class Solution {
public:
    /**
     * @param formatString: the format string
     * @param queryStrings: the query strings
     * @return: judge isMatch
     */
    vector<bool> isMatch(string &formatString, vector<string> &queryStrings) {
        // write your code here
        vector<bool> res;
        for (string& s: queryStrings) {
            res.push_back(isMatch(s, formatString));
        }
        return res;
    }

    bool isMatch(const string& s, string p) {
        int n = s.size();
        if (p.size()) {
            p = p[0] == '^' ? p = p.substr(1) : ".*" + p;
            p = p[p.size()-1] == '$' ? p.substr(0,p.size()-1) : p + ".*";
        }
        int m = p.size();
        bool dp[2][m + 1];
        dp[0][0] = true;
        for (int j = 2; j < m + 1; ++j) {
            dp[0][j] = (p[j - 1] == '*' || p[j - 1] == '?') && dp[0][j - 2];
        }
        for (int i = 1; i < n + 1; ++i) {
            for (int j = 0; j < m + 1; ++j) {
                dp[i % 2][j] = false;
                if (j == 0) continue;
                if (s[i - 1] == p[j - 1] || p[j - 1] == '.') {
                    dp[i % 2][j] = dp[(i - 1) % 2][j - 1];
                } else if (p[j - 1] == '*') {
                    if (p[j - 2] != '.' && p[j - 2] != s[i - 1]) {
                        dp[i % 2][j] = dp[i % 2][j - 2];
                    } else {
                        dp[i % 2][j] = dp[i % 2][j - 2] || dp[(i - 1) % 2][j - 2] || dp[(i - 1) % 2][j];
                    }
                } else if (p[j - 1] == '?') {
                    if (s[i - 1] !=  p[j - 2] && p[j - 2] != '.')
                        dp[i % 2][j] = dp[i % 2][j - 2];
                    else
                        dp[i % 2][j] = dp[(i - 1) % 2][j - 2] || dp[i % 2][j - 2];
                } else if (p[j - 1] == '+') {
                    if (s[i - 1] == p[j - 2] || p[j - 2] == '.')
                        dp[i % 2][j] = dp[(i - 1) % 2][j - 2] || dp[(i - 1) % 2][j];
                }
            }
        }
        return dp[n % 2][m];
    }
};
