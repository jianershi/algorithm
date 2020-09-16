/**
 * 1579. Remove Max Number of Edges to Keep Graph Fully Traversable
 * https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/
 * TLE, largely correct. somehow timed out on constant time compared to the solution passed.
 */
class UnionFind {
private:
    unordered_map<int, int> fathers;
    int count = 0;
    
public:
    bool add(int node){
        if (fathers.count(node)) return false;
        fathers[node] = node;
        count++;
        return true;
    }
    
    int find(int x) {
        if (fathers[x] != x)
            fathers[x] = find(fathers[x]);
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
        unordered_map<int, unordered_set<int>> m1;
        unordered_map<int, unordered_set<int>> m2;
        unordered_map<int, unordered_set<int>> m3;
        for (auto &e: edges) {
            if (e[0] == 1) { m1[e[1]].insert(e[2]); m1[e[2]].insert(e[1]); }
            if (e[0] == 2) { m2[e[1]].insert(e[2]); m2[e[2]].insert(e[1]); }
            if (e[0] == 3) { m3[e[1]].insert(e[2]); m3[e[2]].insert(e[1]); }
        }
    
        UnionFind uf;
        int res = 0;
        for (int i = 1; i <= n; ++i) {uf.add(i);}
        
        for (auto& n: m3) {
            for (auto& neighbor: n.second) {
                res += uf.unionTwo(n.first, neighbor) ? 1 : 0;
            }
        }
        
        UnionFind uf1 = uf;
        UnionFind uf2 = uf;
        
        for (auto& n: m1) {
            for (auto& neighbor: n.second) {
                res += uf1.unionTwo(n.first, neighbor) ? 1 : 0;
            }
        }
        
        for (auto& n: m2) {
            for (auto& neighbor: n.second) {
                res += uf2.unionTwo(n.first, neighbor) ? 1 : 0;
            }
        }
        
        if (uf1.getCount() != 1 || uf2.getCount() != 1) return -1;
        
        return edges.size() - res;
        
    }

};