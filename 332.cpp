/**
 * 332. restoreArray
 * https://www.lintcode.com/problem/restorearray
 * solution: https://github.com/wisdompeak/LintCode/blob/9efeb3a2dd7543f977c4be69204741031bf0d03a/DP/332.Restore-Array/Readme.md
 * tle
 * dp[i][0]: what is the total number of ways at ith digit that has sum % 3 == 0
 * answer: dp[n][0]
 * intial condition: dp[0][0] = 1 there is 1 way at digit 0 to have sum % 3 == 0 -> empty set
 */
class Solution {
public:
    /**
     * @param n: the length of the array.
     * @param l: the least limit for element.
     * @param r: the largest limit for element.
     * @return: return the ways to restore the array.
     */
    int restoreArray(int n, int l, int r) {
        // write your code here.
        long long MOD = 1e9+7;
        long long n0 = 0, n1 = 0, n2 = 0;
        for (long long i = l; i <=r ; ++i) {
            if (i % 3 == 0) n0++;
            if (i % 3 == 1) n1++;
            if (i % 3 == 2) n2++;
        }
        int dp[n + 1][3];
        memset(dp, 0, sizeof dp);
        dp[0][0] = 1;
        for (int i = 1; i < n + 1; ++i) {
            dp[i][0] = ((dp[i - 1][0] * n0) % MOD + (dp[i - 1][1] * n2) % MOD + (dp[i - 1][2] * n1) % MOD) % MOD;
            dp[i][1] = ((dp[i - 1][0] * n1) % MOD + (dp[i - 1][1] * n0) % MOD + (dp[i - 1][2] * n2) % MOD) % MOD;
            dp[i][2] = ((dp[i - 1][0] * n2) % MOD + (dp[i - 1][1] * n1) % MOD + (dp[i - 1][2] * n0) % MOD) % MOD;
        }
        return dp[n][0] % MOD;
    }
};