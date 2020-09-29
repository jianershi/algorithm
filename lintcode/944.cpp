/**
 * 944. Maximum Submatrix
 * https://www.lintcode.com/problem/maximum-submatrix/description
 *
 * 等同令狐冲老师的解法。
 * 更加简洁的版本。
 * 枚举上下边界。o(n^2)
 * 算每一列的前缀和可以边枚举边算。o(n) 每次上边届扩展的时候前缀和清零，下边界扩展的时候不需要重复计算上边届到下边界的前缀和因为已经存起来了。
 * 总体时间复杂度 o(n^3)
 */
class Solution {
public:
    /**
     * @param matrix: the given matrix
     * @return: the largest possible sum
     */
    int maxSubmatrix(vector<vector<int>> &matrix) {
        // write your code here
        if (!matrix.size() || !matrix[0].size()) return 0;
        int n = matrix.size(), m = matrix[0].size();
        
        int res = INT_MIN;
        for (int top = 0; top < n; ++top) {
            vector<int> prefixSum(m, 0);
            for (int bottom = top; bottom < n; ++bottom) {
                int minimum = 0, nowSum = 0;
                for (int j = 0; j < m; ++j){
                    nowSum += prefixSum[j] + matrix[bottom][j];
                    res = max(res, nowSum - minimum);
                    prefixSum[j] += matrix[bottom][j];
                    minimum = min(minimum, nowSum);
                }
            }
        }
        return res;
        
    }
};