"""
471. Top K Frequent Words
https://www.lintcode.com/problem/top-k-frequent-words/description?_from=ladder&&fromId=37

hash map: o(n) time  o(n) extra space


idea:
only record the maximum kth occurance of words in the heap, keep the minmum occurance
if incoming words occurance > min occurance for the current kth most frequent words
discard the minimum occurance of words, update

heap: min heap, but sorting key will be freq1 < freq2 word1 > word2 because we want to keep the smaller alphabetical order
create heap: o(nlogk)

dump heap: o(klogk)

total o((n+k)logk)
"""
import heapq
class Pair:
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word
    
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq

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
            if len(heap) < k:
                heapq.heappush(heap, Pair(freq, word))
            else:
                if heap and Pair(freq,word) > heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, Pair(freq, word))
        
        
        res = []
        for _ in range(k):
            pair = heapq.heappop(heap)
            res.append(pair.word)
        return res[::-1]