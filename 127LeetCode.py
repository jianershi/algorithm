"""
127. Word Ladder
https://leetcode.com/problems/word-ladder/
"""
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not endWord or not wordList or len(wordList) < 1:
            return 0
        
        wordList = set(wordList)
        wordList.add(beginWord)
        
        queue = deque([(beginWord, 1)])
        distance = {beginWord: 1}
        
        while queue:
            now, dist = queue.popleft()
            if now == endWord:
                return dist
            for word in self.next_word(now, wordList):
                if word in distance:
                    continue
                queue.append((word, dist + 1))
                distance[word] = dist + 1
                
        return 0
    
    def next_word(self, word, wordList):
        candidates = []
        n = len(word)
        for i in range(n):
            prefix = word[:i]
            postfix = word[i + 1:]
            for c in "abcdefghijklmnopqrstuvwxyz":
                if word[i] == c:
                    continue
                new_word = prefix + c + postfix
                if new_word in wordList:
                    candidates.append(new_word)
        return candidates
            