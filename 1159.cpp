/**
 * 1159. Longest Common Prefix III
 * https://www.lintcode.com/problem/longest-common-prefix-iii/description
 * memory limit exceeded
 */
class TrieNode{
public:
    unordered_map<char, TrieNode*> children;
    bool isWord = false;
    int dist = 0;
    int id = -1;
    unordered_set<int> prefix_word;
};

class Trie{
private:
    TrieNode* trie = new TrieNode();
    
public:    
    map<pair<int, int>, int> dist;
    void add(string word, int id) {
        TrieNode* node = trie;
        for (char& c: word) {
            if (!node->children.count(c)) {
                node->children[c] = new TrieNode();
                node->children[c]->dist = node->dist + 1;
            }
            node->prefix_word.insert(id);
            node = node->children[c];
        }
        node->prefix_word.insert(id);
        node->isWord = true;
        node->id = id;
    }
    
    void query(void){
        query(trie);
    }
    
    void query(TrieNode *node) {
        for (const int& w1: node->prefix_word) {
            for (const int& w2: node->prefix_word) {    
                dist[make_pair(w1, w2)] = max(dist[make_pair(w1, w2)], node->dist);
            }
        }
        
        for (auto& child: node->children) {
            query(child.second);
        }
    }
    
};

class Solution {
private:
    Trie trie;
public:
    /**
     * @param arr: string array
     * @param query: query array
     * @return: return  LCP ans array
     */
    vector<int> queryLCP(vector<string> &arr, vector<vector<int>> &query) {
        // write your code here
        int n = arr.size();
        for (int i = 0; i < n; ++i) {
            trie.add(arr[i], i);
        }
        
        trie.query();
        
        int m = query.size();
        vector<int> res;
        for (int i = 0; i < m; ++i) {
            res.push_back(trie.dist[make_pair(query[i][0], query[i][1])]);
        }
        return res;
        
        
    }
};