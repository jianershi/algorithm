/**
 * 845. Greatest Common Divisor
 * https://www.lintcode.com/problem/greatest-common-divisor/description
 * Euclidean algorithm https://cp-algorithms.com/algebra/euclid-algorithm.html
 *
 **/
class Solution {
public:
    int gcd (int a, int b) {
        return b ? gcd (b, a % b) : a;
    }
};
