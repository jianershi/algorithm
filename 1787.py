"""
1787. Google Suggestion (Map Reduce)
https://www.lintcode.com/problem/google-suggestion-map-reduce/description
"""
'''
Definition of Document
class Document:
    def __init__(self, word, count):
        self.word = word
        self.count = count
'''
from Mr_tools import Document
import heapq
class GoogleSuggestion:
    # @param {Document} value is a document and value have two attributes(word and count)
    def mapper(self, _, value):
        # Write your code here
        # Please use 'yield key, value' here
        # key is prefix and value is Pair
        for i in range(len(value.word)):
            yield value.word[:i + 1], value

    def __init__(self):
        self.heap = []
    # @param key is from mapper
    # @param values is a list of document
    def reducer(self, key, values):
        # Write your code here
        yield key, sorted(values, key=lambda x: (-x.count, x.word))[:10]
