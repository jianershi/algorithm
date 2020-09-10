/**
 * 206. Interval Sum
 * https://www.lintcode.com/problem/interval-sum/description
 *
 * efficient segment tree
 * https://codeforces.com/blog/entry/18051
 *
 * prefix sum will be easier, but i want to practise segment tree
 */

/**
 * Definition of Interval:
 * classs Interval {
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */
class SegmentTree {
private:
    static const int N = 1e6;
    int n;
    
public:
    long long t[N * 2];
    SegmentTree(int n) : n(n) {}
    
    void build(){
        for (int i = n - 1; i > 0; --i) t[i] = t[i<<1] + t[i<<1 | 1];
    }
    
    void modify(int p, int val) {
        for (t[p += n] = val; p > 1; p >>= 1) t[p >> 1] = t[p] + t[p^1];
    }
    
    long long query(int l, int r) {
        long long res = 0;
        for (l += n, r += n; l < r; l >>= 1, r >>= 1) {
            if (l&1) res += t[l++];
            if (r&1) res += t[--r];
        }
        return res;
    }
};

class Solution {
public:
    /**
     * @param A: An integer list
     * @param queries: An query list
     * @return: The result list
     */
    vector<long long> intervalSum(vector<int> &A, vector<Interval> &queries) {
        // write your code here
        int n = A.size();
        SegmentTree tree(n);
        for (int i = 0; i < n; ++i) {
            tree.t[n + i] = A[i];
        }
        tree.build();
        vector<long long> res;
        for (auto& q: queries) {
            res.push_back(tree.query(q.start, q.end + 1));
        }
        return  res;
        
    }
};