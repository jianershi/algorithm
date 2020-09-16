"""
120. Word Ladder
https://www.lintcode.com/problem/word-ladder/description
用一个不需要分层遍历的方法。用distance当visited用。
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
        dict.add(end)
        queue = deque([start])
        distance = {start: 1}
        length = 0

        while queue:
            node = queue.popleft()
            if node == end:
                return distance[node]
            for next_word in self.next_word(node):
                if next_word in dict and next_word not in distance:
                    queue.append(next_word)
                    distance[next_word] = distance[node] + 1

        return -1

    def next_word(self, word):
        word_list = set()
        for i in range(len(word)):
            left = word[:i]
            center = word[i]
            right = word[i+1:]
            for char in "abcdefghijklmnopqrstuvwxyz":
                if char != center:
                    word_list.add(left + char + right)
        # print ("length: {}: {}".format(len(word_list), word_list))
        return word_list
