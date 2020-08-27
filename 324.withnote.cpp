/**
324. Regular Expression Search
https://www.lintcode.com/problem/regular-expression-search/description
solution based on DP solution of leetcode 10:
https://leetcode.com/problems/regular-expression-matching/
https://leetcode.com/problems/regular-expression-matching/discuss/5651/Easy-DP-Java-Solution-with-detailed-Explanation
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

        // check if string begin with ^ or end with $, prepend/append .* to convert the problem to full string matching instead of partial matching.
        if (p.size()) {
            p = p[0] == '^' ? p = p.substr(1) : ".*" + p;
            p = p[p.size()-1] == '$' ? p.substr(0,p.size()-1) : p + ".*";
        }
        int m = p.size();
        bool dp[n + 1][m + 1];
        memset(dp, false, sizeof dp);
        dp[0][0] = true;

        // .*.*.* or .?.?.? will match and empty string
        for (int j = 2; j < m + 1; ++j) {
            dp[0][j] = (p[j - 1] == '*' || p[j - 1] == '?') && dp[0][j - 2];
        }
        for (int i = 1; i < n + 1; ++i) {
            for (int j = 1; j < m + 1; ++j) {
                if (s[i - 1] == p[j - 1] || p[j - 1] == '.') { // case 1. match actual char or .(any char)
                    dp[i][j] = dp[i - 1][j - 1];
                } else if (p[j - 1] == '*') { // case 2. *
                    if (p[j - 2] != '.' && p[j - 2] != s[i - 1]) { // case 2.1 not matching
                        dp[i][j] = dp[i][j - 2];
                    } else { // case 2.2 match actual char or .
                        dp[i][j] = dp[i][j - 2] ||  dp[i - 1][j];
                        // choose to match none || choose to match >= 1
                        // notice we don't have to have a seperate case for match exactly 1 char, because this case
                        // is covered in dp[i - 1][j] <- which means matches 0 or more chars. if it happens to match 0
                        // that means at least we have 1 match at current char i - 1
                    }
                } else if (p[j - 1] == '?') { // case 3: ?
                    if (s[i - 1] !=  p[j - 2] && p[j - 2] != '.') // case 3.1 not matching
                        dp[i][j] = dp[i][j - 2];
                    else    // case 3.2 match actual char or .
                        dp[i][j] = dp[i - 1][j - 2] || dp[i][j - 2]; // choose to match none || choose to match exactly 1
                } else if (p[j - 1] == '+') { // case 4: +
                    if (s[i - 1] == p[j - 2] || p[j - 2] == '.') // case 4: + (has to match >= 1)
                        dp[i][j] = dp[i - 1][j - 2] || dp[i - 1][j]; // choase to match exactly 1 || choose to match > 1
                        // notice we need a seperate ase to match exactly 1 char (different than the case discussed in *).
                        // because + inherently requires >= 1 so we cannot just say dp[i][j] = dp[i - 1][j] which implies
                        // curr char match AND prev match as well: essentially requiring at least 2 match from current char
                        // i - 1 forward. while + will satify as long as there is >= 1 match.
                }
            }
        }
        return dp[n][m];
    }
};
