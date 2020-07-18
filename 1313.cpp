/*
1313. Bipartite Graph
https://www.lintcode.com/problem/bipartite-graph/description?_from=contest&&fromId=96
*/
#include <algorithm>
#include <iostream>
#include <unordered_set>
#include <vector>
using namespace std;
class Solution {
private:
    void dfs(int index, vector<vector<int>> &graph, unordered_set<int> path, int* min_dist) {
        if (path.size() >= 2 && path.size() <= graph.size() - 2) {
            int group_one = 0;
            int group_two = 0;
   
            for (int i = 0; i < graph.size(); ++i){
                if (path.find(i) == path.end()) {
                    for (int j = i + 1; j < graph.size(); ++j) {
                        if (path.find(j) == path.end()) {
                            group_two = max({group_two, min(graph[i][j], graph[j][i])});    
                        }
                    }
                } else {
                    for (int j = i + 1; j < graph.size(); ++j) {
                        if (path.find(j) != path.end()) {
                            group_one = max({group_one, min(graph[i][j], graph[j][i])});
                        }
                    }
                }
            }
            
            *min_dist = min(*min_dist, max(group_two, group_one));
        }

        for (int i = index + 1; i < graph.size(); ++i) {
            path.insert(i);
            dfs(i, graph, path, min_dist);
            path.erase(i);
        }
    }

public:

    /**
     * @param graph: graph edge value
     * @return: return the minium length of graph
     */
    int getMiniumValue(vector<vector<int>> &graph) {
        // write your code here.
        int n = graph.size();
        if (n < 4) {
            return -1;
        }

        int min_distance = INT_MAX;
        
        dfs(0, graph, unordered_set<int> {0}, &min_distance);
    
        return min_distance;
    }

};

int main() {
    Solution s;
    vector<vector<int>> graph = 
    {
        {0,270,60,20},
        {270,0,35,90},
        {60,35,0,100},
        {20,90,100,0}
    };
    s.getMiniumValue(graph);
}