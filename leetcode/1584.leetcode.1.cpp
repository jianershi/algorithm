/**
 * 1584. Min Cost to Connect All Points
 * https://leetcode.com/problems/min-cost-to-connect-all-points/
 * prim
 *
 * prim V*E(prim)
 * total time complexity V*E for building adj + V*E(prim) = V*E
 *
 * https://cp-algorithms.com/graph/mst_prim.html
 * https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/
 * https://leetcode.com/problems/min-cost-to-connect-all-points/discuss/843958/C%2B%2B-Classic-Minimum-Spanning-Tree-or-Prim's-%2B-Kruskal(TLE-idk-why)-or-Mini-Tutorial
 */
class Solution {
private:
    int minNode(int n, int key[], bool mstSet[]) {
        int min = INT_MAX, min_index = -1;
        for (int i = 0; i < n; ++i) {
            if (!mstSet[i] && key[i] < min) {
                min = key[i];
                min_index = i;
            }
        }
        return min_index;
    }
    
    int solve(int n, vector<vector<int>>& edges) {
        int parent[n];
        int key[n];
        bool mstSet[n];
        for (int i = 0; i < n; ++i) {
            mstSet[i] = false;
            key[i] = INT_MAX;
        }
        parent[0] = -1;
        key[0] = 0;
        for (int i = 0; i < n; ++i) {
            int u = minNode(n, key, mstSet);
            mstSet[u] = true;
            for (int v = 0; v < n; ++v) {
                if (!mstSet[v] && edges[u][v] < key[v]) {
                    parent[v] = u;
                    key[v] = edges[u][v];
                }
            }
        }
        int res = 0;
        for (int i = 1; i < n; ++i){
            res += edges[parent[i]][i];
        }
        return res;
    }
    
public:
    int minCostConnectPoints(vector<vector<int>>& points) {
        
        int n = points.size();
        
        vector<vector<int>> edges(n, vector<int>(n));
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                edges[i][j] = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]);
            }
        }
        
        return solve(n, edges);
    }
};