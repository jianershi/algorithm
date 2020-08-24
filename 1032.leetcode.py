"""
1032. Stream of Characters
https://leetcode.com/problems/stream-of-characters/
LTE
"""
class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}
        self.word = None
        self.prefix = set()
        
class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = TrieNode()
        self.q = deque()
        for word in words:
            root = self.trie
            for c in word:
                root.children[c] = root.children.get(c, TrieNode())
                root = root.children[c]
                root.prefix.add(c)
            root.is_word = True
            root.word = word
    
    def query(self, letter: str) -> bool:
        if letter in self.trie.children:
            self.q.append(self.trie)
        
        n = len(self.q)
        ok = False
        for _ in range(n):
            top = self.q.popleft()
            if letter in top.children:
                top = top.children[letter]
                if top.is_word:
                    ok = True
                self.q.append(top)
        
        return ok
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)