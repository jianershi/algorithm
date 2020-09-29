/**
 * 1042. Toeplitz Matrix
 * https://www.lintcode.com/problem/toeplitz-matrix/description
 */
class Solution {
public:
    /**
     * @param matrix: the given matrix
     * @return: True if and only if the matrix is Toeplitz
     */
    bool isToeplitzMatrix(vector<vector<int>> &matrix) {
        // Write your code here
        int n = matrix.size(), m = matrix[0].size();
        
        for (int i = 1; i < n; ++i)
            for (int j = 1; j < m; ++j)
                if (matrix[i][j] != matrix[i - 1][j - 1])
                    return false;
        
        return true;
        
    }
};