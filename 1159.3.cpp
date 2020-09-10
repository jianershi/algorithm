/**
 * 1159. Longest Common Prefix III
 * https://www.lintcode.com/problem/longest-common-prefix-iii/description
 * 
 * efficient segment tree
 * https://codeforces.com/blog/entry/18051
 *
 * the segment tree here is redefined as [0,1) <- LCP from sorted str[0] to sorted str[1]
 * the redefinition is necessary because everything after it, [0,3)-> LCP str[0] to str[3] is minimum of LCPs inside this range.
 * but LCP of str[i] to *itself* str[i], i.e. [i,i] will always = len(str[i]), which is not suitable for segment tree
 */
class SegmentTree {
private:
    static const int N = 1e5;  // limit for array size
    int n;  // array size
    
public:
    int t[2 * N]; // segment tree array
    SegmentTree(int n) : n(n) {}
    
    void build() {  // build the tree
      for (int i = n - 1; i > 0; --i) t[i] = min(t[i<<1],t[i<<1|1]);
    }
    
    int query(int l, int r) {  // min on interval [l, r)
      int res = INT_MAX;
      for (l += n, r += n; l < r; l >>= 1, r >>= 1) {
        if (l&1) res = min(res,t[l++]);
        if (r&1) res = min(res,t[--r]);
      }
      return res;
    }

    void insertLeaves(vector<int>& leaves) {
        for (int i = 0; i < n; ++i) {
            t[n + i] = leaves[i];
        }
    }
};

class Solution {
public:
    vector<int> queryLCP(vector<string> &arr, vector<vector<int>> &q){
        // write your code here
        
        int n = arr.size();
        SegmentTree tree(n);
        
        int m = q.size();

        //record original index
        vector<pair<string, int>> newAry;
        for (int i = 0; i < n; ++i)
            newAry.push_back(make_pair(arr[i],i));

        //sort by lexiographical order
        sort(newAry.begin(), newAry.end(), [&](auto &a, auto &b){return a.first < b.first;});

        //build map from old index->new index so when doing query, easy to find locations inside the new query
        //the segment tree is also built on new query
        vector<int> idxToNew(n);
        for (int i = 0; i < n; ++i)
            idxToNew[newAry[i].second] = i;
        
        //build lcp array str[i] to str[i - 1], which is the minimum range allowed on the segment tree (using the redefined definiton (see top))
        vector<int> LCPArray = buildLCPArray(newAry);

        //insert leaves
        tree.insertLeaves(LCPArray);

        //build tree from leaves to root
        tree.build();
        
        vector<int> res;
        for (auto&singleQ: q) {
            int x = idxToNew[singleQ[0]]; // find new index
            int y = idxToNew[singleQ[1]];
            if (x > y) swap(x, y); // make sure first index is smaller
            if (x == y) res.push_back(arr[singleQ[0]].size()); // handle the case not handled by the redefiniton of the segment tree->namely LCP to oneself
            else res.push_back(tree.query(x,y)); // standard segment tree query
        }
        return res;
    }
    
    vector<int> buildLCPArray(vector<pair<string, int>> &arr) {
        int n = arr.size();
        vector<int> LCPArray;
        for (int i = 0; i < n - 1; ++i) {
            int mn = min(arr[i + 1].first.size(), arr[i].first.size());
            int lcp = 0;
            for (int j = 0; j < mn; ++j) {
                if (arr[i + 1].first[j] == arr[i].first[j])
                    lcp = j + 1;
                else
                    break;
            }
            LCPArray.push_back(lcp);
        }
        LCPArray.push_back(0); //to match size to n, meaning empty string compared to last item has LCP of 0
        
        return LCPArray;
    }
};