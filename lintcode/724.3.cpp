/**
 * 724. Minimum Partition
 * https://www.lintcode.com/problem/minimum-partition/description
 */
class Solution {
public:
    /**
     * @param nums: the given array
     * @return: the minimum difference between their sums 
     */
    int findMin(vector<int> &nums) {
        // write your code here
        int totalSum = accumulate(nums.begin(), nums.end(), 0);
        int n = nums.size();
        bool dp[n + 1][totalSum/2 + 1];
        memset(dp, 0, sizeof dp);
        dp[0][0] = true;
        for (int i = 1; i < n + 1; ++i) {
            for (int j = 0; j < totalSum/2 + 1; ++j) {
                dp[i][j] = dp[i - 1][j];
                if (j >= nums[i - 1])
                    dp[i][j] |= dp[i - 1][j - nums[i - 1]];
            }
        }
        
        int maxWeight = 0;
        for (int k = totalSum/2; ~k; --k) {
            if (dp[n][k] == true) {
                maxWeight = k;
                break;
            }
        }
        return abs(totalSum - 2 * maxWeight);
    }
};