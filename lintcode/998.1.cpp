/**
 * 998. Construction Queue
 * https://www.lintcode.com/problem/construction-queue/description
 * using segment tree
 */
#include <bits/stdc++.h>

class SegmentTree {
private:
    static const int N = 1e7;
    int n;
    int t[4 * N];

public:
    SegmentTree(int n): n(n) {
        memset(t, 0, sizeof t);
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
    
    void update(int v, int tl, int tr, int pos) {
        if (tl == tr) {
            t[v]--;
        } else {
            int tm = tl + (tr - tl) / 2;
            if (pos <= tm)
                update(v*2, tl, tm, pos);
            else
                update(v*2+1, tm+1, tr, pos);
            t[v] = t[v*2] + t[v*2+1];
        }
    }

    int findLastSpot(int v, int tl, int tr, int count) {
        if (tl == tr)
            return tl;
        int tm = tl + (tr - tl) / 2;
        if (count <= t[v*2])
            return findLastSpot(v * 2, tl, tm, count);
        else
            return findLastSpot(v * 2 + 1, tm + 1, tr, count - t[v*2]);
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
            int firstAvailable = st.findLastSpot(1, 0, n - 1, arr2[original_idx] + 1);
            res[firstAvailable] = arr[i].first;
            st.update(1, 0, n - 1, firstAvailable);
        }
        return res;
        
    }
};

