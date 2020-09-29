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
        if (a == 0) return 50;
        bool pos = a > 0;
        if (a < 0) a = -a;
        
        vector<int> digits;
        while (a) {
            digits.push_back(a % 10);
            a /= 10;
        }
        
        long long res = 0;
        bool inserted = false;
        if (pos) {
            for (int i = digits.size() - 1; ~i; --i) {
                if (!inserted && digits[i] <= 5) {
                    res = 10 * res + 5;
                    inserted = true;
                }
                res = 10 * res + digits[i];
            }
        } else {
            for (int i = digits.size() - 1; ~i; --i) {
                if (!inserted && digits[i] >= 5) {
                    res = 10 * res + 5;
                    inserted = true;
                }
                res = 10 * res + digits[i];
            }
        }
        return pos ? res : -res;
    }
};