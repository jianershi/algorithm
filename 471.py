"""
471. Top K Frequent Words
https://www.lintcode.com/problem/top-k-frequent-words/description?_from=ladder&&fromId=37

hash map: o(n) time  o(n) extra space
heap: o(n) time heapify o(n) extra space
top k -> o(klogn)
"""
import heapq
class Solution:
    """
    @param words: an array of string
    @param k: An integer
    @return: an array of string
    """
    def topKFrequentWords(self, words, k):
        # write your code here
        map = {}
        for w in words:
            map[w] = map.get(w, 0) + 1
        
        heap = []
        for word, freq in map.items():
            heap.append((-freq, word))
        heapq.heapify(heap)
        
        res = []
        for _ in range(k):
            _, word = heapq.heappop(heap)
            res.append(word)
        return res