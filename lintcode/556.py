"""
556. Standard Bloom Filter
https://www.lintcode.com/problem/standard-bloom-filter/
"""
import random
class StandardBloomFilter:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        # do intialization if necessary
        self.BASE = k * 100000
        self.bit_array = [0] * self.BASE
        self.random_seed = []
        for i in range(k):
            self.random_seed.append(random.randint(1,100000))

    """
    @param: word: A string
    @return: nothing
    """
    def add(self, word):
        # write your code here
        self.calculate_hash(word, set=True)


    """
    @param: word: A string
    @return: True if contains word
    """
    def contains(self, word):
        # write your code here
        return self.calculate_hash(word, set=False)

    def calculate_hash(self, word, set=False):
        # print(self.bit_array)
        for seed in self.random_seed:
            hash_code = 0
            for c in word:
                hash_code = (hash_code * 31 + ord(c) + seed) % self.BASE
            if set:
                self.bit_array[hash_code] = 1
                # print(self.bit_array)
            if not set:
                if not self.bit_array[hash_code]:
                    return False
        return True
