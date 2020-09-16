/**
1249. Minimum Remove to Make Valid Parentheses
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
**/
class Solution {
public:
    string minRemoveToMakeValid(string s) {
        int count = 0;
        string result;
        for (char&c : s) {
            if (c == '(') {
                result += c;
                count += 1;
            } else if (c == ')') {
                if (count) {
                    result += c;
                    count -= 1;
                }
            } else {
                result += c;
            }
        }
        reverse(result.begin(), result.end());
        s = result;
        count = 0;
        result.clear();
        for (char&c : s) {
            if (c == ')') {
                result += c;
                count += 1;
            } else if (c == '(') {
                if (count) {
                    result += c;
                    count -= 1;
                }
            }  else {
                result += c;
            }
        }
        reverse(result.begin(), result.end());
        return result;
    }
    // string one_pass(string s) {
    //     int count = 0;
    //     string result;
    //     for (char&c : s) {
    //         if (c == '(') {
    //             result += c;
    //             count += 1;
    //         } else if (c == ')') {
    //             if (count) {
    //                 result += c;
    //                 count -= 1;
    //             }
    //         }
    //     }
    //     return result;
    // }
};
