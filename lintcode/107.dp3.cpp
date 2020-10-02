/**
 * 107. Word Break
 * https://www.lintcode.com/problem/word-break/description?_from=ladder&&fromId=160
 * dp. using max len of dictionary word
 * O(n * maxLen)
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
        
        int maxLen = 0;
        for (auto& w: wordSet) {
            maxLen = max(maxLen, (int)w.size());
        }
        
        for (int i = 1; i < n + 1; ++i) {
            for (int len = 1; len <= min(i, maxLen); ++len) {
                dp[i] = dp[i] || (dp[i - len] && wordSet.count(s.substr(i - len, len)));
            }
        }
        return dp[n];
    }
};