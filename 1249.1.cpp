/**
1249. Minimum Remove to Make Valid Parentheses
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
a bit cleaner.
two pass. 
O(2n)
first pass take care of extra )
second pass take care of extra (
**/
class Solution {
public:
    string minRemoveToMakeValid(string s) {
        s = onePass(s, 0);
        reverse(s.begin(), s.end());
        s = onePass(s, 1);
        reverse(s.begin(), s.end());
        return s;
    }
    string onePass(string s, int flag) {
        char paren1, paren2;
        if (flag == 0) {
            paren1 = '(';
            paren2 = ')';
        } else {
            paren1 = ')';
            paren2 = '(';  
        }
        int count = 0;
        string result;
        for (char&c : s) {
            if (c == paren1) {
                result += c;
                count += 1;
            } else if (c == paren2) {
                if (count) {
                    result += c;
                    count -= 1;
                }
            } else {
                result += c;
            }
        }
        return result;
    }
};
