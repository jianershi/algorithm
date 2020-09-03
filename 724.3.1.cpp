/**
 * 724. Minimum Partition
 * https://www.lintcode.com/problem/minimum-partition/description
 * 1d array
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
        bool dp[totalSum/2 + 1];
        memset(dp, 0, sizeof dp);
        dp[0] = true;
        for (int i = 1; i < n + 1; ++i) {
            for (int j = totalSum / 2; j - nums[i - 1] >= 0; --j) {
                dp[j] |= dp[j - nums[i - 1]];
            }
        }
        
        int maxWeight = 0;
        for (int k = totalSum/2; ~k; --k) {
            if (dp[k] == true) {
                maxWeight = k;
                break;
            }
        }
        return abs(totalSum - 2 * maxWeight);
    }
};