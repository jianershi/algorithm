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
        
        for (int j = 0; j < m; ++j) {
            int base = matrix[0][j];
            for (int i = 0; i + j < min(m,n); ++i) {
                if (matrix[i][i+j] != base)
                    return false;
            }    
        }
        
        for (int i = 0; i < n; ++i) {
            int base = matrix[i][0];
            for (int j = 0; i + j < min(m,n); ++j) {
                if (matrix[i+j][j] != base)
                    return false;
            }
        }
        
        return true;
        
    }
};