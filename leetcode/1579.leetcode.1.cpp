/**
 * 1579. Remove Max Number of Edges to Keep Graph Fully Traversable
 * https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/
 */
class UnionFind {
private:
    // unordered_map<int, int> fathers;
    vector<int> fathers;
    int count = 0;
    
public:
    UnionFind(int n) {
        for (int i = 0; i <= n; ++i)
            fathers.push_back(i);
        count = n;
    }
    
    int find(int x) {
        if (fathers[x] != x) {
            fathers[x] = find(fathers[x]);
        }
        return fathers[x];
    }
    
    bool unionTwo(int a, int b) {
        int fa = find(a);
        int fb = find(b);
        if (fa == fb) return false;
        fathers[fa] = fb;
        count--;
        return true;
    }
    
    int getCount() {
        return count;
    }
};

class Solution {
public:
    int maxNumEdgesToRemove(int n, vector<vector<int>>& edges) {
        sort(edges.begin(), edges.end(), [&](auto &a, auto &b) {return a[0] > b[0];});
        //don't use sort(edges.begin(), edges.end(), std::greater<>()); will TLE
        //
        UnionFind uf1(n), uf2(n);
        
        int res = 0;
        
        for (auto& e: edges) {
            switch(e[0]) {
                case 3:
                    res += uf1.unionTwo(e[1], e[2]) | uf2.unionTwo(e[1], e[2]);
                    break;
                case 1:
                    res += uf1.unionTwo(e[1], e[2]);
                    break;
                case 2:
                    res += uf2.unionTwo(e[1], e[2]);
                    break;
            }
        }
        
        return uf1.getCount() == 1 && uf2.getCount() == 1 ? edges.size() - res : -1;
        
    }

};