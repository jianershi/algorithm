/**
724. Minimum Partition
https://www.lintcode.com/problem/minimum-partition/description

01背包
算法班2020 C27 01背包变形

第二种dp定义
dp[i][j]: considering previous i items, whether it is possible to fill sum j

dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]] if j >= nums[i - 1]

dp[0][0] = True
dp[i][0] = False

answer
max(dp[n])

1d array 不知道为啥能过。。python的挂了。
**/
#include <numeric>
class Solution {
public:
    /**
     * @param nums: the given array
     * @return: the minimum difference between their sums 
     */
    int findMin(vector<int> &nums) {
        // write your code here
        if (nums.size() == 0) {
            return 0;
        }
        
        int n = nums.size();
        int total_sum = std::accumulate(nums.begin(), nums.end(), 0);
        int target = total_sum / 2;
        
        vector<bool> dp(target + 1, false);
        dp[0] = true;
        
        for (int i = 1; i <= n; ++i) {
            for (int j = target; j >= nums[i - 1]; --j) {
                dp[j] = dp[j] || dp[j - nums[i - 1]];
            }
        }
        
        for (int j = target; j >= 0; --j) {
            if (dp[j]) {
                return total_sum - 2 * j;
            }
        }
    }
};