/**
 * 1219. Heaters
 * https://www.lintcode.com/problem/heaters/leaderboard
 */
class Solution {
public:
    /**
     * @param houses: positions of houses
     * @param heaters: positions of heaters
     * @return: the minimum radius standard of heaters
     */
    int findRadius(vector<int> &houses, vector<int> &heaters) {
        // Write your code here
        sort(heaters.begin(), heaters.end());
        int minDist = -INT_MAX;
        for (int& house: houses) {
            auto it = lower_bound(heaters.begin(), heaters.end(), house);
            int right_dist = it < heaters.end() ? *it - house : INT_MAX;
            int left_dist = it - 1 >= heaters.begin() ? house - *--it : INT_MAX;
            
            minDist = max(minDist, min(left_dist, right_dist));
        }
        return minDist;
    }
};