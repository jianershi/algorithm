/**
 * 107. Word Break
 * https://www.lintcode.com/problem/word-break/description?_from=ladder&&fromId=160
 * dp 另外一种dp..定义一样
 */
class Solution {
public:
    /**
     * @param s: A string
     * @param wordSet: A dictionary of words dict
     * @return: A boolean
     */
    bool wordBreak(string &s, unordered_set<string> &wordSet) {
        // write your code here
        int n = s.size();
        bool dp[n + 1];
        memset(dp, false, sizeof dp);
        dp[0] = true;
        
        for (int i = 0; i < n + 1; ++i) {
            for (auto& w: wordSet) {
                if (i + w.size() <= n) {
                    dp[i + w.size()] = dp[i + w.size()] || (dp[i] && s.substr(i, w.size()) == w);
                }
            }
        }
        return dp[n];
    }
};