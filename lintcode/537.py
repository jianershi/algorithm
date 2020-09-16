"""
537. N-Gram (Map Reduce)
https://www.lintcode.com/problem/n-gram-map-reduce/description
"""
class NGram:

    # @param {int} n a integer
    # @param {str} string a string
    def mapper(self, _, n, string):
        # Write your code here
        # Please use 'yield key, value' here
        left, right = 0, n -1
        m = len(string)
        while right < m:
            yield string[left: right + 1], 1
            left += 1
            right += 1



    # @param key is from mapper
    # @param values is a set of value with the same key
    def reducer(self, key, values):
        # Write your code here
        # Please use 'yield key, value' here
        count = 0
        for _ in values:
            count += 1
        yield key, count
