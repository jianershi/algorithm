/**
 * 386. Longest Substring with At Most K Distinct Characters
 * https://www.lintcode.com/problem/longest-substring-with-at-most-k-distinct-characters/leaderboard 
 */
class Solution {
public:
    /**
     * @param s: A string
     * @param k: An integer
     * @return: An integer
     */
    int lengthOfLongestSubstringKDistinct(string &s, int k) {
        // write your code here
        int count = 0, n = s.size(), l = 0, maxLen = 0;
        int seen[256];
        memset(seen, false, sizeof seen);
        for (int r = 0; r < n; ++r) {
            if (seen[s[r]]++ == 0) count++;
            while (l < r && count > k) {
                if (--seen[s[l++]] == 0) count--;
            }
            if (count <= k) maxLen = max(maxLen, r - l + 1);
        }
        return maxLen;
    }
};