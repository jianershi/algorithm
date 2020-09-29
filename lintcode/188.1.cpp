/**
 * 188. Insert five
 * https://www.lintcode.com/problem/insert-five/description
 */
class Solution {
public:
    /**
     * @param a: A number
     * @return: Returns the maximum number after insertion
     */
    int InsertFive(int a) {
        // write your code here
        if (a >= 0) {
            string s = to_string(a);
            int i;
            for (i = 0; i < s.size(); ++i) {
                if (s[i] <= '5')
                    break;
            }
            return stoi(s.substr(0, i) + "5" + s.substr(i));
        } else {
            string s = to_string(-a);
            int i;
            for (i = 0; i < s.size(); ++i) {
                if (s[i] >= '5')
                    break;
            }
            return -stoi(s.substr(0, i) + "5" + s.substr(i));
        }
    }
};