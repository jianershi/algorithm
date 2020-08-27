/**
324. Regular Expression Search
https://www.lintcode.com/problem/regular-expression-search/description
solution based on DP solution of leetcode 10:
https://leetcode.com/problems/regular-expression-matching/
https://leetcode.com/problems/regular-expression-matching/discuss/5651/Easy-DP-Java-Solution-with-detailed-Explanation

说实话这个优化很恶心。。不明不白的。可读性变差很多。
uses at instead of [] to include boundary checking
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
            p = p.at(0) == '^' ? p = p.substr(1) : ".*" + p;
            p = p.at(p.size()-1) == '$' ? p.substr(0,p.size()-1) : p + ".*";
        }
        int m = p.size();
        int now = 0, old = 0;
        bool dp[2][m + 1];
        dp[0][0] = true;
        for (int j = 2; j < m + 1; ++j) {
            dp[now][j] = (p.at(j - 1) == '*' || p.at(j - 1) == '?') && dp[now][j - 2];
        }
        for (int i = 1; i < n + 1; ++i) {
            old = now;
            now = 1 - now;
            for (int j = 0; j < m + 1; ++j) {
                dp[now][j] = false;
                if (j == 0) continue;
                if (s.at(i - 1) == p.at(j - 1) || p.at(j - 1) == '.') {
                    dp[now][j] = dp[old][j - 1];
                } else if (p.at(j - 1) == '*') {
                    if (p.at(j - 2) != '.' && p.at(j - 2) != s.at(i - 1)) {
                        dp[now][j] = dp[now][j - 2];
                    } else {
                        dp[now][j] = dp[now][j - 2] || dp[old][j - 2] || dp[old][j];
                    }
                } else if (p.at(j - 1) == '?') {
                    if (s.at(i - 1) !=  p.at(j - 2) && p.at(j - 2) != '.')
                        dp[now][j] = dp[now][j - 2];
                    else
                        dp[now][j] = dp[old][j - 2] || dp[now][j - 2];
                } else if (p.at(j - 1) == '+') {
                    if (s.at(i - 1) == p.at(j - 2) || p.at(j - 2) == '.')
                        dp[now][j] = dp[old][j - 2] || dp[old][j];
                }
            }
        }
        return dp[now][m];
    }
};
