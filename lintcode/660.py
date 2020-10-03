"""
660. Read N Characters Given Read4 II - Call multiple times
https://www.lintcode.com/problem/read-n-characters-given-read4-ii-call-multiple-times

The read4 API is already defined for you.
@param buf a list of characters
@return an integer
you can call Reader.read4(buf)
"""
class Solution:
    def __init__(self):
        self.buf = [None] * 4
        self.next_w = 0
        self.next_r = 0
        
    # @param {char[]} buf destination buffer
    # @param {int} n maximum number of characters to read
    # @return {int} the number of characters read
    def read(self, buf, n):
        # Write your code here
        i = 0
        while i < n:
            if self.next_r == self.next_w:
                self.next_r, self.next_w = 0, Reader.read4(self.buf)
                if self.next_w == self.next_r:
                    break
            buf[i], i, self.next_r = self.buf[self.next_r], i + 1, self.next_r + 1
        return i