/**
1567. Maximum Length of Subarray With Positive Product
https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/

dp[i]: max len of subarray that satisfies the condition that ending in ith position.
for >0:
    dp[i] = dp[i - 1] + 1
for 0:
    dp[i] = 0
for <0:
    dp[i] = max(0, dp[last_neg_i] + i - 1 - last_neg_i + 1);
                      ^
                      prev result before hit last neg number
                                    -----------------------
                                    ^ len between current index and last neg
                   ----------------------------------------
                   ^ select this number
                ^not select this number (can just ignore this one)

result max(dp)

initial condition: dp[0] = 0
**/
class Solution {
public:
    int getMaxLen(vector<int>& nums) {
        int max_len = 0, last_neg_i = -1,n = nums.size();
        vector<int> dp(n + 1);
        dp[0] = 0;
        for (int i = 1; i < n + 1; ++i) {
            if (nums[i - 1] == 0) {
                dp[i] = 0; 
                last_neg_i = -1;
            } else if (nums[i - 1] > 0) {
                dp[i] = dp[i - 1] + 1;
            } else {
                if (last_neg_i == -1) dp[i] = 0;
                else dp[i] = dp[last_neg_i] + i - 1 - last_neg_i + 1;
                last_neg_i = i - 1;
            }
        }
        return *max_element (dp.begin(), dp.end());
    }
};