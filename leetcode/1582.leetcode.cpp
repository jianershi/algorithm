/**
 * 1582. Special Positions in a Binary Matrix
 * https://leetcode.com/contest/weekly-contest-206/problems/special-positions-in-a-binary-matrix/
 */
class Solution {
public:
    int numSpecial(vector<vector<int>>& mat) {
        int n = mat.size(), m = mat[0].size();
        vector<int> row(n, 0);
        vector<int> col(m, 0);
        vector<pair<int,int>> one;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j){
                if (mat[i][j] != 1) continue;
                one.push_back(make_pair(i,j));
                row[i]++;
                col[j]++;
            }
        }
        int res = 0;
        for (auto& o: one) {
            res += row[o.first] == 1 && col[o.second] == 1 ? 1 : 0;
        }
        return res;
    }
};