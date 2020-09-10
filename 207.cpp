/**
 * 207. Interval Sum II
 * https://www.lintcode.com/problem/interval-sum-ii/description
 *
 * efficient segment tree
 * https://codeforces.com/blog/entry/18051
 *
 */
class SegmentTree{
private:
    static const int N = 1e6;
    int n;

public:
    long long t[N * 2];
    SegmentTree(int n) : n(n) {}
    void build() {
        for (int i = n - 1; i > 0; --i) t[i] = t[i << 1] + t[i << 1 | 1];
    }
    
    void modify(int p, int val) {
        for (t[p += n] = val; p > 1; p >>= 1) t[p >> 1] = t[p] + t[p^1];
    }
    
    long long query(int l, int r){
        long long res = 0;
        for (l += n, r += n; l < r; l >>= 1, r >>= 1) {
            if (l&1) res += t[l++];
            if (r&1) res += t[--r];
        }
        return res;
    }
};
class Solution {
private:
    SegmentTree tree;
    
public:
    /* you may need to use some attributes here */

    /*
    * @param A: An integer array
    */
    Solution(vector<int> A) : tree(A.size()) {
        // do intialization if necessary
        int n = A.size();
        for (int i = 0; i < n; ++i) {
            tree.t[n + i] = A[i];
        }
        tree.build();
    }

    /*
     * @param start: An integer
     * @param end: An integer
     * @return: The sum from start to end
     */
    long long query(int start, int end) {
        // write your code here
        return tree.query(start, end + 1);
    }

    /*
     * @param index: An integer
     * @param value: An integer
     * @return: nothing
     */
    void modify(int index, int value) {
        // write your code here
        tree.modify(index, value);
    }
};