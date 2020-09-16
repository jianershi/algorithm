/**
 * 1542. Find Longest Awesome Substring
 * https://leetcode.com/problems/find-longest-awesome-substring/
 */
class Solution {
public:
    int longestAwesome(string s) {
        unordered_map<int, int> seen = {{0, -1}}; //states, index
        int state = 0, n = s.size(), maxLen = 0;
        for (int i = 0; i < n; ++i) {
            int shift = string("0123456789").find(s[i]);
            state ^= 1 << shift;
            
            if (seen.count(state)) maxLen = max(maxLen, i - seen[state]);

            for (int j = 0; j < 10; ++j) {
                int test = state ^ 1 << j;
                if (seen.count(test)) maxLen = max(maxLen, i - seen[test]);
            }
            
            if (!seen.count(state)) seen[state] = i;
        }
        return maxLen;
    }
};