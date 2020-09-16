/**
1542. Find Longest Awesome Substring
https://leetcode.com/problems/find-longest-awesome-substring/

thought process:
find the longest possible palindrone?


**/
class Solution {
public:
    int longestAwesome(string s) {
        int curr = 0; //state
        unordered_map<int, int> seen{{0, -1}};
        int max_len = 1;
        for (int i = 0; i < s.size(); ++i) {
            int d = s[i] - '0';
            curr ^= 1 << d;
            if (!seen.count(curr)) {
                seen[curr] = i;
            }
            max_len = max(max_len, i - seen[curr]);
            for (int j = 0; j < 10; ++j) {
                if (seen.count(curr ^ (1 << j))) {
                    max_len = max(max_len, i - seen[curr ^ (1 << j)]);
                }
            }
        }
        return max_len;
    }
};