/**
 * 1583. Count Unhappy Friends
 * https://leetcode.com/problems/count-unhappy-friends/
 * brute force
 */
class Solution {
public:
    int unhappyFriends(int n, vector<vector<int>>& preferences, vector<vector<int>>& pairs) {
        unordered_map<int, int> pair_map;
        for (auto& pair: pairs) {
            pair_map[pair[0]] = pair[1];
            pair_map[pair[1]] = pair[0];
        }
        
        unordered_map<int, unordered_map<int, int>> prefer;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < preferences[i].size(); ++j) {
                prefer[i][preferences[i][j]] = j;
            }
        }
        
        int res = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (i == j) continue;
                if (prefer[i][j] < prefer[i][pair_map[i]] && prefer[j][i] < prefer[j][pair_map[j]] ) {
                    res++;
                    break;
                }
            }
        }
            
        return res;
    }
};