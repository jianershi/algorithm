/**
1032. Stream of Characters
https://leetcode.com/problems/stream-of-characters/
reverse char -> trie
**/
class TrieNode {
public:
    map<char, TrieNode* > children;
    bool is_word = false;
};
class StreamChecker {
private:
    TrieNode * const root = new TrieNode();
    deque<char> stream;
public:
    StreamChecker(vector<string>& words) {
        for (string& w : words) {
            TrieNode *node = root;
            reverse(w.begin(), w.end());
            for (char& c: w) {
                if (node->children.count(c) == 0) node->children[c] = new TrieNode();
                node = node->children[c];
            }
            node->is_word = true;
        }
    }
    
    bool query(char c) {
        stream.push_front(c);
        TrieNode *node = root;
        for (char& c: stream) {
            if (node->children.count(c) == 0) return false;
            node = node->children[c];
            if (node->is_word) return true;
        }
        return false;
    }
};