/**
 * 402. Continuous Subarray Sum
 * https://www.lintcode.com/problem/continuous-subarray-sum/description
 */
class Solution {
public:
    /*
     * @param A: An integer array
     * @return: A list of integers includes the index of the first number and the index of the last number
     */
    vector<int> continuousSubarraySum(vector<int> &A) {
        // write your code here
        int minimum = 0, min_idx = -1, s = 0, e = 0, nowSum = 0, n = A.size(), maximum = INT_MIN;
        for (int i = 0; i < n; ++i) {
            nowSum += A[i];
            if (nowSum - minimum > maximum) {
                maximum = nowSum - minimum;
                e = i;
                s = min_idx + 1;
            }
            if (nowSum < minimum) {
                minimum = nowSum;
                min_idx = i;
            }
        }
        return {s, e};
    }
};