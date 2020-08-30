/**
1568. Minimum Number of Days to Disconnect Island
https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/
TLE
**/
class Solution {
private:
    bool isOneIsland(vector<vector<int>> &grid) {
        int n = grid.size(), m = grid[0].size();
        int count = 0;
        // vector<vector<bool>> vis = (n, vector<bool>(m, false));
        set<pair<int,int>> vis;
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j)
                if (grid[i][j] == 1 && !vis.count(make_pair(i,j))) {
                    bfs(grid, i, j, vis);
                    ++count;
                }
        return count == 1;
    }
    
    void bfs(vector<vector<int>> &grid, int x, int y, set<pair<int,int>>& v) {
        int n = grid.size(), m = grid[0].size();
        int delta_x[4] = {0, 0, -1, 1};
        int delta_y[4] = {-1, 1, 0, 0};
        deque<pair<int,int>> q;
        q.push_back(make_pair(x,y));
        v.insert(make_pair(x,y));
        while (!q.empty()) {
            pair<int,int> f = q.front(); q.pop_front();
            for (int i = 0; i < 4; ++i) {
                int nx = f.first + delta_x[i], ny = f.second + delta_y[i];
                if (!isValid(nx, ny, grid, v)) continue;
                v.insert(make_pair(nx,ny));
                q.push_back(make_pair(nx,ny));
            }
        }
        return;
    }
    
    bool isValid(int x, int y, vector<vector<int>> &grid, set<pair<int,int>> v) {
        if (x < 0 || x >= grid.size()) return false;
        if (y < 0 || y >= grid[0].size()) return false;
        if (v.count(make_pair(x,y))) return false;
        if (grid[x][y] == 0) return false;
        return true;
    }
public:
    int minDays(vector<vector<int>>& grid) {
        if (!isOneIsland(grid)) return 0;
        for (int i = 0; i < grid.size(); ++i) {
            for (int j = 0; j < grid[0].size(); ++j) {
                if (grid[i][j] == 1) {
                    grid[i][j] = 0;
                    if (!isOneIsland(grid)) return 1;
                    grid[i][j] = 1;
                }
            }
        }
        return 2;
    }
};