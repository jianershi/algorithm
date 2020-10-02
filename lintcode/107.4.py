"""
107. Word Break
https://www.lintcode.com/problem/word-break/description?_from=ladder&&fromId=160
trie

trie build and query O(log(avgLenofWord)) estimate O(1)
dfs 2^n 

so trie here is really useless, could just use a dictionary

"""
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def add(self, word):
        node = self.root
        for c in word:
            node.children[c] = node.children.get(c, TrieNode())
            node = node.children[c]
        
        node.is_word = True
        node.wordLen = len(word)
    
    def query(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_word
        
class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}
        self.wordLen = 0
        
class Solution:
    """
    @param s: A string
    @param wordSet: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, wordSet):
        # write your code here
        trie = Trie()
        for word in wordSet:
            trie.add(word)
        
        return self.dfs(0, s, trie)
        
    def dfs(self, index, s, trie):
        n = len(s)
        if (index == len(s)):
            return True
        
        for i in range(index, n):
            if not trie.query(s[index:i+1]):
                continue
            if self.dfs(i+1, s, trie):
                return True
        
        return False