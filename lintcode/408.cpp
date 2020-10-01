/**
 * 408. Add Binary
 * https://www.lintcode.com/problem/add-binary/description
 */
class Solution {
public:
    /**
     * @param a: a number
     * @param b: a number
     * @return: the result
     */
    string addBinary(string &a, string &b) {
        // write your code here
        string res;
        int carry = 0;
        for (int i = a.size() - 1, j = b.size() - 1; i >= 0 || j >= 0; --i,--j ) {
            int d = (i >= 0 ? int(a[i]) - '0' : 0) + (j >= 0 ? int(b[j]) - '0' : 0) + carry;
            res += to_string(d % 2);
            carry = d / 2;
        }
        res += carry ? "1" : "";
        return string(res.rbegin(), res.rend());
    }
};