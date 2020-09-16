/**
1569. Number of Ways to Reorder Array to Get Same BST
https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/
solution: https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/discuss/819369/C%2B%2B-Just-using-recursion-very-Clean-and-Easy-to-understand-O(n2)
**/

class Solution {
private:
    vector<vector<long long>> pascalTriangle;
    
    void buildPascalTriangle(vector<int> &nums, long long mod) {
        int n = nums.size();
        pascalTriangle.resize(n + 1);
        for (int i = 0; i < n + 1; ++i) {
            pascalTriangle[i] = vector<long long> (i + 1, 1);
            for (int j = 1; j < i; ++j) {
                pascalTriangle[i][j] = (pascalTriangle[i - 1][j - 1] + pascalTriangle[i - 1][j]) % mod;
            }
        }
    }
    
    int dfs(vector<int>& nums, long long mod) {
        int n = nums.size();
        if (n <= 2) return 1;
        
        vector<int> left, right;
        for (int i = 1; i < n; ++i) {
            if (nums[i] < nums[0]) left.push_back(nums[i]);
            else right.push_back(nums[i]);
        }
        int left_len = left.size(), right_len = right.size();
        int left_res = dfs(left, mod) % mod, right_res = dfs(right, mod) % mod;
        
        return (((pascalTriangle[n - 1][left_len] * left_res) % mod) * right_res) % mod;   
    }
    
public:
    int numOfWays(vector<int>& nums) {
        long long mod = 1e9+7;
        int n = nums.size();
        buildPascalTriangle(nums, mod);
        return dfs(nums, mod) % mod - 1;
    }
};