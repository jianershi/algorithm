/**
 * 952. Largest Component Size by Common Factor
 * https://leetcode.com/problems/largest-component-size-by-common-factor/
 *
 * pretty dirty solution using union find and prime factorization 
 *
 * 235. Prime Factorization
 * https://www.lintcode.com/problem/prime-factorization/
 */
class UnionFind{
private:
    unordered_map<int, int> fathers; // factor->parent
    unordered_map<int, int> memberCount;
    
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

    void addPrime(int x) {
        if (fathers.count(x) == 0) {
            fathers[x] = x;
        }
    }

    
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
        memberCount[bf] += memberCount[af];
        memberCount.erase(af);
        return true;
    }

public:
    void add(int num) {
        vector<int> f = primeFactorization(num);
        int n = f.size();
        if (n == 0) return;
        addPrime(f[0]);
        memberCount[find(f[0])]++;
        for (int i = 1; i < n; ++i)  {
            addPrime(f[i]);
            unionTwo(f[i], f[i - 1]);
        }
    }

    unordered_map<int, int>& getMemberCount() {return memberCount;}
};
    
    
class Solution {
public:
    int largestComponentSize(vector<int>& A) {
        UnionFind uf;
        for (int& num : A) {
            uf.add(num);
        }
        return max_element(uf.getMemberCount().begin(), uf.getMemberCount().end(), [](const auto& a, const auto& b) {return a.second < b.second;})->second;
    }
};