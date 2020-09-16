"""
634. Word Squares
https://www.lintcode.com/problem/word-squares/description
brute force:
check every posible combination. there are 1000 words of at most length 5.
C(1000, 5) ~ 1000^5 possible combinations * the time to check each.

with pruning.
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.words_under_prefix = set()

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, words):
        for word in words:
            node = self.root
            for c in word:
                node.children[c] = node.children.get(c, TrieNode())
                node = node.children[c]
                node.words_under_prefix.add(word)
            node.is_word = True

    def search_prefix(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return []
            node = node.children[c]
        return node.words_under_prefix

class Solution:
    def __init__(self):
        self.root = TrieNode()

    """
    @param: words: a set of words without duplicates
    @return: all word squares
    """
    def wordSquares(self, words):
        # write your code here
        if not words:
            return []
        n = len(words[0])

        trie = Trie()
        trie.add(words)

        results = []
        for word in words: #choose starting word
            self.dfs_word_square(trie, words, n, [word], results)

        return results
    """
    b a l l
    a r e a
    l e a d
    l a d y
    """
    """
    @param: words: a set of words without duplicates
    @param: n: size of the matrix
    @param: path: current search path
    @results: save successful combination into results
    @return: None
    """
    def dfs_word_square(self, trie, words, n, path, results):
        cur_word_square_index = len(path)
        if cur_word_square_index == n:
            results.append(list(path))
            return


        """
        pruning
        say path = [ball] , then check if there is any words starting with a, l, l
        if not, don't even have to search further.
        """
        for i in range(cur_word_square_index, n):
            prefix = [word[i] for word in path]
            if not trie.search_prefix(prefix):
                return

        #search any word starting with a
        prefix = [word[cur_word_square_index] for word in path]

        words_with_prefix = trie.search_prefix(prefix)

        for word in words_with_prefix:
            path.append(word)
            self.dfs_word_square(trie, words, n, path, results)
            path.pop()

s = Solution()
words = ["area","lead","wall","lady","ball"]

print(s.wordSquares(words))
