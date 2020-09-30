/**
 * 838. Subarray Sum Equals K
 * https://www.lintcode.com/problem/subarray-sum-equals-k/description
 */
#include <bits/stdc++.h>

class Solution {
public:
    /**
     * @param nums: a list of integer
     * @param k: an integer
     * @return: return an integer, denote the number of continuous subarrays whose sum equals to k
     */
    int subarraySumEqualsK(vector<int> &nums, int k) {
        // write your code here
        int n = nums.size(), nowSum = 0;
        unordered_map<int, int> prefixSum = {{0, 1}}; //prefixsum, occurance count
        int res = 0;
        for (int i = 0; i < n; ++i) {
            nowSum += nums[i];
            if (prefixSum.count(nowSum - k)) res += prefixSum[nowSum - k];
            prefixSum[nowSum]++;
        }
        
        return res;
    }
};