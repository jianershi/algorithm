"""
132. Word Search II
https://www.lintcode.com/problem/word-search-ii/description
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word_under_prefix = set()

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, words):
        for word in words:
            node = self.root
            for c in word:
                node.children[c] = node.children.get(c, TrieNode())
                node = node.children[c]
                node.word_under_prefix.add(word)
            node.is_word = True

    def search_prefix(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return []
            node = node.children[c]
        return node.word_under_prefix

    def contains_word(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_word

DIRECTIONS = [
    (0, 1),
    (0, -1),
    (-1, 0),
    (1, 0)
]

class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        # write your code here
        if not board or not board[0]:
            return []

        results = set()
        n = len(board)
        m = len(board[0])

        trie = Trie()
        trie.add(words)

        for i in range(n):
            for j in range(m):
                self.search_word(board, i, j, trie, [board[i][j]], set([(i,j)]), results)

        return list(results)

    def search_word(self, board, i, j, trie, path, visited, results):
        prefix_list = trie.search_prefix(path)
        if prefix_list == []:
            return
        if trie.contains_word(path):
            found_word = "".join(list(path))
            if found_word not in results:
                results.add(found_word)

        for delta_x, delta_y in DIRECTIONS:
            next_x, next_y = i + delta_x, j + delta_y
            if self.is_valid(board, next_x, next_y, visited, path):
                path.append(board[next_x][next_y])
                visited.add((next_x, next_y))
                self.search_word(board, next_x, next_y, trie, path, visited, results)
                path.pop()
                visited.remove((next_x, next_y))

    def is_valid(self, board, next_x, next_y, visited, path):
        n = len(board)
        m = len(board[0])

        if (next_x, next_y) in visited:
            return False

        if not (0 <= next_x < n and 0 <= next_y < m):
            return False

        return True


s = Solution()
board = ["doaf","agai","dcan"]
words = ["dog","dad","dgdg","can","again"]
print(s.wordSearchII(board, words))
