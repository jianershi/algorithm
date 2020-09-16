/**
1568. Minimum Number of Days to Disconnect Island
https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/
BFS
used 2d vectors instead of set for visited. pass
**/
class Solution {
private:
    bool isOneIsland(vector<vector<int>> &grid) {
        int n = grid.size(), m = grid[0].size();
        int count = 0;
        vector<vector<bool>> vis(n, vector<bool>(m, false));
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j)
                if (grid[i][j] == 1 && !vis[i][j]) {
                    bfs(grid, i, j, vis);
                    ++count;
                }
        return count == 1;
    }
    
    void bfs(vector<vector<int>> &grid, int x, int y, vector<vector<bool>>& v) {
        vector<int> DELTA_X = {0, 0, -1, 1};
        vector<int> DELTA_Y = {-1, 1, 0, 0};
        
        int n = grid.size(), m = grid[0].size();
        deque<pair<int,int>> q;
        q.push_back(make_pair(x,y));
        v[x][y] = true;
        while (!q.empty()) {
            pair<int,int> f = q.front(); q.pop_front();
            for (int i = 0; i < 4; ++i) {
                int nx = f.first + DELTA_X[i], ny = f.second + DELTA_Y[i];
                if (!isValid(nx, ny, grid, v)) continue;
                v[nx][ny] = true;
                q.push_back(make_pair(nx,ny));
            }
        }
        return;
    }
    
    bool isValid(int x, int y, vector<vector<int>> &grid, vector<vector<bool>>& v) {
        if (x < 0 || x >= grid.size()) return false;
        if (y < 0 || y >= grid[0].size()) return false;
        if (v[x][y]) return false;
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