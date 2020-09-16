"""
473. Add and Search Word - Data structure design
https://www.lintcode.com/problem/add-and-search-word-data-structure-design/description
Input:
  addWord("bad")
  addWord("dad")
  addWord("mad")
  search("pad")
  search("bad")
  search(".ad")
  search("b..")
Output:
  false

use Trie to store the word.
for normal serach, search through children until find it.
for search containing '.', it becomes dfs search for all its children
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
    """
    @param: word: Adds a word into the data structure.
    @return: nothing
    """
    def addWord(self, word):
        # write your code here
        node = self.root
        for c in word:
            node.children[c] = node.children.get(c, TrieNode())
            node = node.children[c]
        node.is_word = True

    """
    @param: word: A word could contain the dot character '.' to represent any one letter.
    @return: if the word is in the data structure.
    """
    def search(self, word):
        # write your code here
        return self.search_dfs(word, 0, self.root)

    """
    @param: word: A word could contain the dot character '.' to represent any one letter.
    @param: i: index in word
    @param: node: node to start searching
    @return: if the word is in the data structure.
    """
    def search_dfs(self, word, i, node):
        if i == len(word):
            return node.is_word
        if word[i] != '.':
            if word[i] not in node.children:
                return False
            return self.search_dfs(word, i + 1, node.children[word[i]])

        for child in node.children:
            if self.search_dfs(word, i + 1, node.children[child]):
                return True

        return False
