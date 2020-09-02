/**
 * 1219. Heaters
 * https://www.lintcode.com/problem/heaters/description
 * greedy/ 2pointers
 * left pointer->sorted houses
 * right pointer->sorted heaters
 * for the next house, it is possible to choose the prev heater as the possible heater.
 * e.x. 
 * houses  1 2 3 
 *         | | /
 * heaters 1 2 100000
 * 
 * that's why there is break statement to 
 *     1) prevent increment of right pointer
 *     2) the pointer points to the optimizal heater for the current house
 * right pointer will increase in a monotonous fashion.
 * 
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
        sort(houses.begin(), houses.end());
        int n = houses.size(), m = heaters.size(), minDist = -INT_MAX;
        for (int i = 0, j = 0; i < n; ++i) {
            for (; j < m - 1; ++j) {
                int curr = abs(houses[i] - heaters[j]);
                int next = abs(houses[i] - heaters[j + 1]);
                if (curr < next) break;
            }
            minDist = max(minDist, abs(houses[i] - heaters[j]));
        }
        return minDist;
    }
};
