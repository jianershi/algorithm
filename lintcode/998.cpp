/**
 * 998. Construction Queue
 * https://www.lintcode.com/problem/construction-queue/note/190361
 *
 * TLE
 *
 * 1) sort from big->small
 * 2) fill the big slot first
 * 3) whatever need to be filled need to check available slot, if it is occupied->must been filled before this round, and since numbers were filled from big->small, that means those filled will be bigger than the current number->so unavailable.
 * 4) find the first available spot that will satisfies i - unavailable = count
 * 5) fill it, mark unavaialble 
 *
 * O(nlogn) sort
 * O(n) <- every time check availability
 * total O(nlogn + n^2)
 */
class Solution {
public:
    /**
     * @param n: The array sum
     * @param arr1: The size
     * @param arr2: How many numbers smaller than itself 
     * @return: The correct array
     */
    vector<int> getQueue(int n, vector<int> &arr1, vector<int> &arr2) {
        // Write your code here
        vector<pair<int, int>> arr;
        for (int i = 0; i < n; ++i) {
            arr.push_back(make_pair(arr1[i], i));
        }
        vector<int> res(n);
        vector<int> used(n);
        sort(arr.begin(), arr.end(), [&](auto &a, auto &b){return a.first > b.first;});
        for (int i = 0; i < n; ++i) {
            int original_idx = arr[i].second;
            int firstAvailable = findFirstAvailable(used, arr2[original_idx]);
            res[firstAvailable] = arr[i].first;
            used[firstAvailable] = 1;
        }
        return res;
        
    }
    
    int findFirstAvailable(vector<int>& used, int count) {
        int unavailable = 0;
        for (int i = 0; i < used.size(); ++i) {
            if (used[i]) {
                unavailable++;
            } else {
                if (i - unavailable == count)
                    return i;
            } 
        }
        return -1;
    }
};