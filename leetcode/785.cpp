/**
 * 785. Is Graph Bipartite?
 * https://leetcode.com/problems/is-graph-bipartite/
 * dfs
 */
class Solution {
public:
    /**
     * @param graph: the given undirected graph
     * @return:  return true if and only if it is bipartite
     */
    bool isBipartite(vector<vector<int>> &graph) {
        // Write your code here
        int n = graph.size();
        vector<int> colors(n, -1);
        for (int i = 0; i < n; ++i) {
            if (colors[i] == -1)
                if (!dfs(i, graph, colors, 0))
                    return false;
        }
        return true;
    }
    
    bool dfs(int index, vector<vector<int>> &graph, vector<int> &colors, int color) {
        colors[index] = color;
        for (auto &e: graph[index]) {
            if (colors[e] != -1 && colors[e] == color) return false;
            if (colors[e] == -1 && !dfs(e, graph, colors, 1 - color)) return false;
        }
        return true;
    }
};