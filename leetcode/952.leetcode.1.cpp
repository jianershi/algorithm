/**
 * 952. Largest Component Size by Common Factor
 * https://leetcode.com/problems/largest-component-size-by-common-factor/
 *
 * standard union find + prime factorization 
 * union using the number itself and each of their prime factor
 * in the end iterate through all numbers in the original sequence by using find to see if they belong to each other
 *
 * 235. Prime Factorization
 * https://www.lintcode.com/problem/prime-factorization/
 */

class UnionFind{
private:
    unordered_map<int, int> fathers; // factor->parent
    
public:
    int find(int x) {
        if (fathers[x] != x) {
            fathers[x] = find(fathers[x]); 
        }
        return fathers[x];
    }
    
    bool unionTwo(int a, int b) {
        int af = find(a);
        int bf = find(b);
        if (af == bf) return false;
        fathers[af] = bf;
        return true;
    }
    
    void add(int x) {
        if (fathers.count(x) == 0) {
            fathers[x] = x;
        }
    }

};
    
    
class Solution {
private:
    vector<int> primeFactorization(int num) {
        vector<int> factors;
        int up = sqrt(num);
        int k = 2;
        while (k <= up && num > 1) {
            while (num % k == 0) {
                factors.push_back(k);
                num /= k;  
            }
            ++k;
        }

        if (num > 1) factors.push_back(num);

        return factors;
    }
public:
    int largestComponentSize(vector<int>& A) {
        UnionFind uf;
        for (int& num : A) {
            uf.add(num);
            vector<int> factors = primeFactorization(num);
            for (int& f: factors) {
                uf.add(f);
                uf.unionTwo(num, f);
            }
        }
        unordered_map<int, int> count;
        int res = 0;
        for (int& num: A) {
            res = max(res, ++count[uf.find(num)]);
        }
        return res;
        
    }
};