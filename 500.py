"""
500. Inverted Index

https://www.lintcode.com/problem/inverted-index/description?_from=ladder&&fromId=75
"""
'''
Definition of Document
class Document:
    def __init__(self, id, cotent):
        self.id = id
        self.content = content
'''
class Solution:
    # @param {Document[]} docs a list of documents
    # @return {dict(string, int[])} an inverted index
    def invertedIndex(self, docs):
        # Write your code here
        map = {}
        for doc in docs:
            words = doc.content.split()
            for word in words:
                map[word] = map.get(word, set())
                map[word].add(doc.id)

        results = {}
        for key, value in map.items():
            results[key] = sorted(list(value))
        return results
