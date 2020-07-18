/*
256. The Maximum Order
https://www.lintcode.com/problem/the-maximum-order/description?_from=contest&&fromId=96
*/
#include <vector>
#include <iostream>
using namespace std;
class Solution {
public:
    bool isValid(vector<int> onHand, vector<int> &supplier, int demand, int order){
        for (int i = 0; i < order; ++i) {
            onHand.push_back(supplier[i]);
        }
        sort(onHand.begin(), onHand.end());
        int day = 0;
        for (int i = 0; i < onHand.size(); i += demand) {
            for (int j = 0; j < demand; ++j) {
                if ((i + j) < onHand.size() && onHand[i + j] < day) {
                    return false;
                }
            }
            ++day;
        }
        return true;
    }
    /**
     * @param onHand: the expiry days of m units of creamer already in stock
     * @param supplier: the expiry days of n units of creamer available for order
     * @param demand: the maximum units of creamer employees will uses daily
     * @return: the maximum units of creamer the manager can order without waste
     */
    int stockLounge(vector<int> &onHand, vector<int> &supplier, int demand) {
        // write your code here
        int n = onHand.size();
        int m = supplier.size();
        sort(supplier.begin(), supplier.end(), greater<int>());
        int start = 0, end = m;
        while (start + 1 < end) {
            int mid = (start + end) / 2;
            if (isValid(onHand, supplier, demand, mid)) {
                start = mid;
            } else {
                end = mid;
            }
        }
       
        if (isValid(onHand, supplier, demand, end)) {
            return end;
        }
        if (isValid(onHand, supplier, demand, start)) {
            return start;
        }

        return -1;
   }
};

int main() {
    vector<int> onHand = {0, 2, 2};
    vector<int> supplier = {2, 0, 0};
    int demand = 2;
    Solution s;
    cout << s.stockLounge(onHand, supplier, demand) << endl;
}