/**
 * 321. perfect string
 * https://www.lintcode.com/problem/perfect-string/description
 * 周赛
 */
class Solution {
public:
    /**
     * @param s: string need to be transformed
     * @param k: minimum char can be transformed in one operation
     * @return: minimum times to transform all char into '1'
     */
    int perfectString(string &s, int k) {
        // Write your code here
        int n = s.size();
        int counter = 0;
        int l = 0, r = 0;
        for (l = 0; l < n; ++l) {
            if (s[l] == '1') continue;
            for (r = l; r < l + k - 1 && s[r] == '0'; ++r){}
            counter++;
            l = r;
        }
        return counter;
    }
};