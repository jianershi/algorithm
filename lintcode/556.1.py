"""
556. Standard Bloom Filter
https://www.lintcode.com/problem/standard-bloom-filter/
"""
import random
class HashFunction:
    def __init__(self, seed, base):
        self.seed = seed
        self.base = base

    def hash_code(self, word):
        hash_code = 0
        for c in word:
            hash_code = (hash_code * 31 + ord(c) + self.seed) % self.base
        return hash_code

class StandardBloomFilter:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        # do intialization if necessary
        self.BASE = k * 100000
        self.bit_array = [0] * self.BASE
        self.hash_function = []
        for i in range(k):
            self.hash_function.append(HashFunction(random.randint(1,100000),self.BASE))

    """
    @param: word: A string
    @return: nothing
    """
    def add(self, word):
        # write your code here
        for hash_func in self.hash_function:
            self.bit_array[hash_func.hash_code(word)] = 1


    """
    @param: word: A string
    @return: True if contains word
    """
    def contains(self, word):
        for hash_func in self.hash_function:
            if not self.bit_array[hash_func.hash_code(word)]:
                return False
        return True
