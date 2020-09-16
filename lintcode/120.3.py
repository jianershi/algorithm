"""
120. Word Ladder
https://www.lintcode.com/problem/word-ladder/description

双向BFS Dual Directional BFS + lazy loading
"""
from collections import deque
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        # write your code here
        if not start or not end or not dict:
            return 0

        dict.add(start)
        dict.add(end)

        forward_queue = deque([start])
        forward_visited = set([start])
        backward_queue = deque([end])
        backward_visited = set([end])

        distance = 1

        while forward_queue and backward_queue:
            distance += 1
            if self.extend_queue(dict, forward_queue, forward_visited, backward_visited):
                return distance

            distance += 1
            if self.extend_queue(dict, backward_queue, backward_visited, forward_queue):
                return distance

        return 0

    def extend_queue(self, dict, queue, visited, opposite_visited):
        for _ in range(len(queue)):
            now = queue.popleft()
            for neighbor in self.search_graph(now, dict):
                if neighbor in visited:
                    continue
                if neighbor in opposite_visited:
                    return True
                queue.append(neighbor)
                visited.add(neighbor)

    """
    using lazy loading
    """
    def search_graph(self, word, word_list):
        self.graph = {}
        if word in self.graph:
            return self.graph[word]

        self.graph[word] = set()
        for i in range(len(word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                if word[i] == c:
                    continue
                new_word = word[:i] + c + word[i + 1:]
                if new_word not in word_list:
                    continue
                self.graph[word].add(new_word)

        return self.graph[word]
