/**
330. Increasing Number
https://www.lintcode.com/problem/increasing-number/description
**/
class Solution {
private:
    long long res = 0;
public:
    /**
     * @param N:  a positive integer N
     * @return: return a maximum integer less than N, each digit of which must be monotonically increasing.
     */
    long long getIncreasingNumber(long long N) {
        // write your code here
        dfs(N, 0, to_string(N).size(), to_string(N).size(), 0);
        return res;
    }

    bool dfs(long long N, int index, int digit, int n, long long curr) {
        if (digit == 0) {
            res = curr;
            return true;
        }

        for (int i = index; i < n; ++i) {
            for (int j = min(9, 10 - n + index); ~j; --j) {
                if (index > 0 && curr % 10 >= j) continue;
                if (j + curr * 10 > N / pow(10,(n - index - 1))) continue;
                if (i == n - 1 && j + curr * 10 >= N / pow(10,(n - index - 1))) continue;
                if (dfs(N, i + 1, digit - 1, n, curr * 10 + j)) return true;
            }
        }
        return false;
    }
};
