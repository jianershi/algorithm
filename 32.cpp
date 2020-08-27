/**
32. Minimum Window Substring
https://www.lintcode.com/problem/minimum-window-substring/
**/
class Solution {
public:
    /**
     * @param source : A string
     * @param target: A string
     * @return: A string denote the minimum window, return "" if there is no such a string
     */
    string minWindow(string &source , string &target) {
        // write your code here
        int freqT[256] = {0};
        int unique_target_char = 0;
        for (char& c: target) {
            if (++freqT[c] == 1) ++unique_target_char;
        }
        int r = 0, n = source.size();
        int r_l = 0, r_r = n;
        int freqS[256] = {0};
        int matched_char = 0;
        for (int l = 0; l < n; ++l) {
            while (r < n && matched_char < unique_target_char) {
                if (++freqS[source[r]] == freqT[source[r]]) ++matched_char;
                ++r;
            }
            if (matched_char == unique_target_char && (r - 1 - l < r_r - r_l)) {
                r_l = l;
                r_r = r - 1;
            }
            if (--freqS[source[l]] == freqT[source[l]] - 1) --matched_char;
        }
        return r_r != n ? source.substr(r_l, r_r - r_l + 1) : "";
    }
};
