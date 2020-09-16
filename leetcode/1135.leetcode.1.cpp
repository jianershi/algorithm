/**
 * 1135. Connecting Cities With Minimum Cost
 * https://leetcode.com/problems/connecting-cities-with-minimum-cost/
 * a bit fasteer using vector instead of unordered_map
 *
 * similar problem: LintCode 
 * 629. Minimum Spanning Tree
 * https://www.lintcode.com/problem/minimum-spanning-tree/description
 */
class UnionFind {
private:
    vector<int> fathers;
    int count = 0;
    
public:
    UnionFind(int n){
        fathers.resize(n + 1);
    }
    
    int find(int x) {
        if (fathers[x] != x)
            fathers[x] = find(fathers[x]);
        return fathers[x];
    }
    
    bool unite(int a, int b) {
        int af = find(a), bf = find(b);
        if (af == bf) return false;
        fathers[af] = bf;
        count--;
        return true;
    }
    
    void add(int x) {
        if (fathers[x]) return;
        fathers[x] = x;
        count++;
    }
    
    bool united() {return count == 1;}
};

class Solution {
public:
    int minimumCost(int N, vector<vector<int>>& connections) {
        sort(connections.begin(), connections.end(), [&](const vector<int> &a, const vector<int> &b){return a[2] < b[2];});
        
        int res = 0;
        UnionFind uf(N);
        for (int i = 1; i <= N; ++i) {
            uf.add(i);
        }
        for (auto& connection: connections) {
            if (uf.unite(connection[0],connection[1])) res += connection[2];
        }
        
        return uf.united() ? res : -1;
    }
};