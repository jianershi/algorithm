"""
126. Word Ladder II
https://leetcode.com/problems/word-ladder-ii/
"""
from collections import deque
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if not beginWord or not endWord or not wordList or len(wordList) < 1:
            return []
    
        wordList = set(wordList)
        if endWord not in wordList:
            return [] #unreachable

        wordList.add(beginWord)
        distance = self.bfs(beginWord, endWord, wordList)
        if beginWord not in distance:
            return [] #unreachable 
        
        results = []
        self.dfs(beginWord, endWord, [beginWord], wordList, distance, results)
        return results
        
    
    def dfs(self, start, target, path, wordList, distance, results):
        if start == target:
            results.append(list(path))
            return
        
        for word in self.next_word(start, wordList):
            if distance[word] >= distance[start]:
                continue
            path.append(word)
            self.dfs(word, target, path, wordList, distance, results)
            path.pop()
        
    def bfs(self, beginWord, endWord, wordList):
        queue = deque([(endWord, 0)])
        distance = {endWord: 0}
        
        while queue:
            now, dist = queue.popleft()
            for word in self.next_word(now, wordList):
                if word in distance:
                    continue
                queue.append((word, dist + 1))
                distance[word] = dist + 1
                
        return distance
    
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
            
            