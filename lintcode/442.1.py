"""
442. Implement Trie (Prefix Tree)
https://www.lintcode.com/problem/implement-trie-prefix-tree/description
answer modified based on 令狐冲's answer
https://www.jiuzhang.com/solution/implement-trie-prefix-tree/
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:

    def __init__(self):
        # do intialization if necessary
        self.root = TrieNode()

    """
    @param: word: a word
    @return: nothing
    """
    def insert(self, word):
        # write your code here
        node = self.root
        for c in word:
            node.children[c] = node.children.get(c, TrieNode())
            node = node.children[c]
        node.is_word = True

    """
    @param: word: A string
    @return: if the word is in the trie.
    """
    def search(self, word):
        # write your code here
        node = self.find(word)
        return node is not None and node.is_word


    def find(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return None
            node = node.children[c]
        return node
    """
    @param: prefix: A string
    @return: if there is any word in the trie that starts with the given prefix.
    """
    def startsWith(self, prefix):
        # write your code here
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True
