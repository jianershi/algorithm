/**
 * 930. Binary Subarrays With Sum
 * https://leetcode.com/problems/binary-subarrays-with-sum/
 * prefix sum
 */
class Solution {
public:
    int numSubarraysWithSum(vector<int>& A, int S) {
        int n = A.size();
        int nowSum = 0, ans = 0;
        map<int, vector<int>> prefixSum; // prefix_sum: its index
        prefixSum[0].push_back(-1);
        int res;
        for (int i = 0; i < n; ++i) {
            nowSum += A[i];
            if (prefixSum.count(nowSum - S)) res += prefixSum[nowSum - S].size();
            prefixSum[nowSum].push_back(i);
        }
        return res;
    }
};