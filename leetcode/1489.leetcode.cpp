/**
 * 1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
 * https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/
 *
 * https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/discuss/697761/C%2B%2B-Solution-enumerating-edges-with-explanation
 */
class UnionFind {
private:  
    unordered_map<int, int> father;
    int count = 0;
    
public:
    UnionFind(int n) {
        for (int i = 0; i < n; ++i) {
            father[i] = i;
            count++;
        }
    }
    
    int find(int x) {
        if (father[x] != x) {
            father[x] = find(father[x]);
        }
        return father[x];
    }
    
    int unite(int a, int b) {
        int af = find(a), bf = find(b);
        if (af == bf) return false;
        father[af] = bf;
        count--;
        return true;
    }
    
    int getCount() {
        return count;
    }  
};

class Solution {
public:
    vector<vector<int>> findCriticalAndPseudoCriticalEdges(int n, vector<vector<int>>& edges) {
        for (int i = 0; i < edges.size(); ++i) {
            edges[i].push_back(i);
        }
        sort(edges.begin(), edges.end(), [&](const vector<int> &a, const vector<int> &b) {return a[2] < b[2];});
        
        
        vector<int> critical;
        vector<int> pseudoCritical;
        
        int minimumMST = calMST(n, edges);
        
        for (int i = 0; i < edges.size(); ++i) {
            if (minimumMST < calMST(n, edges, i)) critical.push_back(edges[i][3]);
            else if (minimumMST == calMST(n, edges, -1, i)) pseudoCritical.push_back(edges[i][3]);
        }
        
        return {critical, pseudoCritical};
        
    }
    
    int calMST(int n, const vector<vector<int>> &edges, int exclude = -1, int include = -1) {
        UnionFind uf(n);
        int minimumCost = 0;
        int m = edges.size();
        if (include != -1) {
            uf.unite(edges[include][0], edges[include][1]);
            minimumCost += edges[include][2];
        }
        
        for (int i = 0; i < m; ++i) {
            if (i == exclude) continue;
            if (uf.unite(edges[i][0],edges[i][1])) {
                minimumCost += edges[i][2];
            }
        }
        
        return uf.getCount() == 1 ? minimumCost : INT_MAX;
    }
};