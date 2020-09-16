/** 
275. Moving Shed
https://www.lintcode.com/problem/moving-shed/description?_from=contest&&fromId=94
TLE
*/

#include <algorithm>
class Solution {
public:
    /**
     * @param stops: An array represents where each car stops.
     * @param k: The number of cars should be covered.
     * @return: return the minimum length of the shed that meets the requirements.
     */
    int calculate(vector<int> &stops, int k) {
        // write your code here
        if (stops.size() < 2) {
            return 0;
        }
        
        int n = stops.size();
        int m = *std::max_element(stops.begin(), stops.end());
        
        int first_car = *std::min_element(stops.begin(), stops.end());
        int j = first_car;

        unordered_set<int> stop_set(stops.begin(), stops.end());
        int num_of_cars = 0;
        int max_window_size_required = 0;
        for (int i = first_car; i < m + 1; ++i) {
            while (j < m + 1 && num_of_cars < k) {
                if (stop_set.find(j++) != stop_set.end()) {
                    ++num_of_cars;
                }
            }
                

            if (num_of_cars >= k) {
                max_window_size_required = max(max_window_size_required, j - i);
            }
            
            if (stop_set.find(i) != stop_set.end()) {
                --num_of_cars;
            }

        }

        return max_window_size_required;    
    }
};