/**
 * 386. Longest Substring with At Most K Distinct Characters
 * https://www.lintcode.com/problem/longest-substring-with-at-most-k-distinct-characters/leaderboard 
 *
 * this method is not very intuitive because of the boundary condition, using previous two pointer is better
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
        int count = 0, n = s.size(), r = 0, maxLen = 0;
        int seen[256];
        memset(seen, false, sizeof seen);
        for (int l = 0; l < n; ++l) {
            while (r < n && count < k || r < n && count == k && seen[s[r]] != 0) {
                if (seen[s[r]]++ == 0) count++;
                r++;
            }
            if (count <= k) maxLen = max(maxLen, r - l);
            if (--seen[s[l]] == 0) count--;
        }
        return maxLen;
    }
};