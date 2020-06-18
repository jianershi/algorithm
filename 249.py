"""
249. Count of Smaller Number before itself
https://www.lintcode.com/problem/count-of-smaller-number-before-itself/description
"""
import math
class Block:
    def __init__(self):
        self.count = {}
        self.total = 0

class BlockArray:
    def __init__(self, array_range):
        self.array_size = int(math.sqrt(array_range)) + 1
        self.blocks = [
            Block() for _ in range(self.array_size)
        ]

    def add(self, num):
        array_index = num // self.array_size
        index_in_array = num % self.array_size
        self.blocks[array_index].count[index_in_array] = self.blocks[array_index].count.get(index_in_array, 0) + 1
        self.blocks[array_index].total += 1

    def count_smaller(self, num):
        array_index = num // self.array_size
        sum_before_block = 0
        for i in range(array_index):
            sum_before_block += self.blocks[i].total

        count_inside_block = 0
        index_inside_block = num % self.array_size

        for i in range(index_inside_block):
            count_inside_block += self.blocks[array_index].count.get(i, 0)

        return sum_before_block + count_inside_block

class Solution:
    """
    @param A: an integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def countOfSmallerNumberII(self, A):
        # write your code here
        ba = BlockArray(10000)
        results = []

        for num in A:
            results.append(ba.count_smaller(num))
            ba.add(num)

        return results
