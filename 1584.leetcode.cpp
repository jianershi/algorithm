/**
 * 1584. Min Cost to Connect All Points
 * https://leetcode.com/problems/min-cost-to-connect-all-points/
 * union find VE
 * VE * logVE sort
 * total VE*logVE
 */
class UnionFind{
private:
    vector<int> father;
public:
    UnionFind(int n) {
        for (int i = 0; i < n; ++i) {
            father.emplace_back(i);
        }
    }
    
    int find(int x) {
        if (father[x] != x)
            father[x] = find(father[x]);
        return father[x];
    }
    
    bool unite(int a, int b) {
        int fa = find(a), fb = find(b);
        if (fa == fb) return false;
        father[fa] = fb;
        return true;
    }
    
    
};

class Solution {
public:
    int minCostConnectPoints(vector<vector<int>>& points) {
        
        int n = points.size();
        UnionFind uf(n);
        vector<tuple<int, int, int>> edges;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                edges.emplace_back(make_tuple(abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j));
            }
        }
        sort(edges.begin(), edges.end(), [&](auto& a, auto &b){return get<0>(a) < get<0>(b);});
        int res = 0;
        for (auto& e: edges) {
            if (uf.unite(get<1>(e), get<2>(e))) {
                res += get<0>(e);
            }
        }
        return res;
    }
};