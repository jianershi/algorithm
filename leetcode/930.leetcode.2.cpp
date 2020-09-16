/**
 * 930. Binary Subarrays With Sum
 * https://leetcode.com/problems/binary-subarrays-with-sum/
 * prefix sum simpler
 */
class Solution {
public:
    int numSubarraysWithSum(vector<int>& A, int S) {
        int n = A.size();
        int nowSum = 0, ans = 0;
        map<int, int> prefixSum; //prefixSum, count
        prefixSum[0] = 1; // to deal with 1st number equal to target.
        int res = 0;
        for (int i = 0; i < n; ++i) {
            nowSum += A[i];
            if (prefixSum.count(nowSum - S)) res += prefixSum[nowSum - S];
            if (!prefixSum.count(nowSum)) prefixSum[nowSum] = 0;
            prefixSum[nowSum]++;
        }
        return res;
    }
};