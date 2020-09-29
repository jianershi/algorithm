/**
 * 998. Construction Queue
 * using segment tree
 * abbreviated version, condense query and update in the same function
 */
#include <bits/stdc++.h>

class SegmentTree {
private:
    int n;
    vector<int>t;

public:
    SegmentTree(int n): n(n) {
        t.resize(n * 4, 0);
    }
    
    void build(int v, int tl, int tr) {
        if (tl == tr) {
            t[v] = 1;
            return;
        }
        int tm = tl + (tr - tl) / 2;
        build(v * 2, tl, tm);
        build(v * 2 + 1, tm + 1, tr);
        t[v] = t[v * 2] + t[v * 2 +1];
    }


    int findLastAvailableSpotAndOccupy(int v, int tl, int tr, int count) {
        if (tl == tr) {
            t[v] = 0;
            return tl;
        }
        int tm = tl + (tr - tl) / 2;
        int ret;
        if (count <= t[v*2])
            ret = findLastAvailableSpotAndOccupy(v * 2, tl, tm, count);
        else
            ret =  findLastAvailableSpotAndOccupy(v * 2 + 1, tm + 1, tr, count - t[v*2]);
            
        t[v] = t[v*2] + t[v*2 + 1];
        return ret;
    }
    
};

class Solution {
public:
    /**
     * @param n: The array sum
     * @param arr1: The size
     * @param arr2: How many numbers smaller than itself 
     * @return: The correct array
     */
    vector<int> getQueue(int n, vector<int> &arr1, vector<int> &arr2) {
        vector<pair<int, int>> arr;
        for (int i = 0; i < n; ++i) {
            arr.push_back(make_pair(arr1[i], i));
        }
        sort(arr.begin(), arr.end(), [&](auto &a, auto &b){return a.first > b.first;});
        vector<int> res(n);
        
        SegmentTree st(n);
        st.build(1, 0, n - 1);
        
        for (int i = 0; i < n; ++i) {
            int original_idx = arr[i].second;
            //notice here, we directly query and count #of digits smaller than arr2[i] + *1* so that when it returns, we occupy it.
            int firstAvailable = st.findLastAvailableSpotAndOccupy(1, 0, n - 1, arr2[original_idx] + 1);
            res[firstAvailable] = arr[i].first;
        }
        return res;
        
    }
};


