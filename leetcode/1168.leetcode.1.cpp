/**
 * 1168. Optimize Water Distribution in a Village
 * https://leetcode.com/problems/optimize-water-distribution-in-a-village/
 * small optimization on the implementation of UF -> not necessary
 */
class UnionFind {
private:
    vector<int> fathers;
    int count = 0;
    
public:
    UnionFind(int n) {
        for (int i = 0; i < n; ++i) {
            fathers.push_back(i);
        }
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
    int minCostToSupplyWater(int n, vector<int>& wells, vector<vector<int>>& pipes) {
        for (int i = 0; i < wells.size(); ++i){
            pipes.push_back({i + 1, 0, wells[i]});
        }
        
        sort(pipes.begin(), pipes.end(), [&](const vector<int> &a, const vector<int> &b) {return a[2] < b[2];});
        
        int res = 0;
        
        UnionFind uf(n + 1);
        
        for (auto& connection: pipes) {
            res += uf.unite(connection[0], connection[1]) ? connection[2] : 0;
        }
        
        return res;
    }
};