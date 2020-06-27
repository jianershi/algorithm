"""
120. Word Ladder
https://www.lintcode.com/problem/word-ladder/description

双向BFS Dual Directional BFS
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
        graph = self.build_graph(dict)

        forward_queue = deque([start])
        forward_visited = set([start])
        backward_queue = deque([end])
        backward_visited = set([end])

        distance = 1

        while forward_queue and backward_queue:
            distance += 1
            if self.extend_queue(graph, forward_queue, forward_visited, backward_visited):
                return distance

            distance += 1
            if self.extend_queue(graph, backward_queue, backward_visited, forward_queue):
                return distance

        return 0

    def extend_queue(self, graph, queue, visited, opposite_visited):
        for _ in range(len(queue)):
            now = queue.popleft()
            for neighbor in graph[now]:
                if neighbor in visited:
                    continue
                if neighbor in opposite_visited:
                    return True
                queue.append(neighbor)
                visited.add(neighbor)

    def build_graph(self, word_list):
        graph = {}

        for word in word_list:
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if word[i] == c:
                        continue
                    new_word = word[:i] + c + word[i + 1:]
                    if new_word not in word_list:
                        continue
                    graph[word] = graph.get(word, set())
                    graph[word].add(new_word)

        return graph
