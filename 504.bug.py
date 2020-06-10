'''
Definition of Document
class Document:
    def __init__(self, id, cotent):
        self.id = id
        self.content = content
'''
class InvertedIndex:

    # @param {Document} value is a document
    def mapper(self, _, value):
        # Write your code here
        # Please use 'yield key, value' here
        word_list = value.content.split()
        for word in word_list:
            yield word, value.id


    # @param key is from mapper
    # @param values is a set of value with the same key
    def reducer(self, key, values):
        # Write your code here
        # Please use 'yield key, value' here
        result = []
        for value in values:
            if result != [] and result[-1] == value:
                continue
            result.append(value)
        yield key, result
