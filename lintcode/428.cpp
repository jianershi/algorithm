class Solution {
public:
    /**
     * @param x: the base number
     * @param n: the power number
     * @return: the result
     */
    double myPow(double x, long long n) {
        // write your code here
        if (n < 0) { x = 1/x; n = -n; }
        if (n == 0) { return 1; }
        double ans = myPow(x, n / 2);
        if (n % 2 == 1) { return ans * ans * x; }
        return ans * ans;
    }
};