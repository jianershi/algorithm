/**
10. Regular Expression Matching
https://leetcode.com/problems/regular-expression-matching/
**/
class Solution {
public:
    bool isMatch(string s, string p) {
        return isMatch(s, 0, p, 0);
    }

    bool isMatch(string &s, int a, string& p, int b) {
        int n = s.size(), m = p.size();
        if (a == n) return isEmpty(p, b);
        if (b == m) return false;

        if (b + 1 < m && p[b + 1]  == '*') {
            return (charMatch(s, a, p, b) && isMatch(s, a+1, p, b) || isMatch(s, a, p, b+2));
        }
        return charMatch(s, a, p, b) && isMatch(s, a+1, p, b+1);
    }

    bool charMatch(string &s, int a, string&p, int b) {
        return s[a] == p[b] || p[b] == '.';
    }

    bool isEmpty(string&p, int b) {
        int m = p.size();
        if ((m - b) % 2 == 1) return false;
        for (int i = b + 1; i < m; i += 2) {
            if (p[i] != '*') return false;
        }
        return true;
    }
};
