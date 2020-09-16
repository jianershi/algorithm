"""
499. Word Count (Map Reduce)
https://www.lintcode.com/problem/word-count-map-reduce/description
"""
class WordCount:

    # @param {str} line a text, for example "Bye Bye see you next"
    def mapper(self, _, line):
        # Write your code here
        # Please use 'yield key, value'
        word_lists = line.split(" ")
        for word in word_lists:
            yield word, 1

    # @param key is from mapper
    # @param values is a set of value with the same key
    def reducer(self, key, values):
        # Write your code here
        # Please use 'yield key, value'
        yield key, sum(values)
