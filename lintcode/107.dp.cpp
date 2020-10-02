/**
 * 107. Word Break
 * https://www.lintcode.com/problem/word-break/description?_from=ladder&&fromId=160
 * dp
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
        
        for (int i = 1; i < n + 1; ++i) {
            for (auto& w: wordSet) {
                if (i - w.size() >= 0) {
                    dp[i] = dp[i] || (dp[i - w.size()] && s.substr(i - w.size(), w.size()) == w);
                }
            }
        }
        return dp[n];
    }
};