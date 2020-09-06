/**
 * 1576. Replace All ?'s to Avoid Consecutive Repeating Characters
 * https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/
 */
class Solution {
public:
    string modifyString(string s) {
        int n = s.size();
        string lower("abcdefghijklmnopqrstuvwxyz");
        string res = "";
        for (int i = 0; i < n; ++i) {
            if (s[i] == '?') {
                int prev = res == "" ? string::npos : lower.find(res.back());
                int next = i == n - 1 ? string::npos : lower.find(s[i + 1]);
                for (int i = 0; i < 26; ++i) {
                    if (i != prev && i != next) {
                        res += lower[i];
                        break;
                    }
                }
            } else {
                res += s[i];
            }
        }
        return res;
    }
};