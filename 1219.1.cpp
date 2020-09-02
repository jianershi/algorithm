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
            minDist = max(minDist, binarySearch(heaters, house));
        }
        return minDist;
    }
    
    int binarySearch(vector<int> &heaters, int house) {
        int start = 0, end = heaters.size() - 1;
        int minDist = INT_MAX;
        while (start + 1 < end) {
            int mid = start + (end - start) / 2;
            if (house > heaters[mid])
                start = mid;
            else
                end = mid;
        }
        minDist = min(abs(heaters[start] - house),abs(heaters[end] - house));
        return minDist;
    }
};