"""
634. Word Squares
https://www.lintcode.com/problem/word-squares/description
brute force:
check every posible combination. there are 1000 words of at most length 5.
C(1000, 5) ~ 1000^5 possible combinations * the time to check each.
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        # self.is_word = False
        self.word = None

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
        self.build_trie(words)

        results = []
        for word in words: #choose starting word
            path = [word]
            self.dfs_word_square(words, n, path, n - 1, results)
            path.pop()

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
    def dfs_word_square(self, words, n, path, length, results):
        if length == 0:
            results.append(list(path))
            return

        prefix_list = []
        for word in path:
            prefix_list.append(word[n - length])

        words_with_prefix  = []
        self.search_prefix_dfs(prefix_list, 0, self.root, words_with_prefix)

        for word in words_with_prefix:
            path.append(word)
            self.dfs_word_square(words, n, path, length - 1, results)
            path.pop()

    """
    @param: words: a set of words without duplicates
    @return: None
    """
    def build_trie(self, words):
        for word in words:
            node = self.root
            for c in word:
                node.children[c] = node.children.get(c, TrieNode())
                node = node.children[c]
            # node.is_word = True
            node.word = word

    """
    @param: prefix_list: a list consists of prefix to search
    @param: index: current location in prefix_list
    @param: node: current node in Trie
    @param: words_with_prefix: results of words with prefix
    @return: None
    """
    def search_prefix_dfs(self, prefix_list, index, node, words_with_prefix):
        if index < len(prefix_list):
            if prefix_list[index] not in node.children:
                return
            self.search_prefix_dfs(prefix_list, index + 1, node.children[prefix_list[index]], words_with_prefix)
            return
        if node.word != None:
            words_with_prefix.append(node.word)
        if not node.children: #define exit if no children
            return
        for child in node.children:
            self.search_prefix_dfs(prefix_list, index + 1, node.children[child], words_with_prefix)



s = Solution()
words = ["area","lead","wall","lady","ball"]

print(s.wordSquares(words))
