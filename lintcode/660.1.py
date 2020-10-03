"""
660. Read N Characters Given Read4 II - Call multiple times
https://www.lintcode.com/problem/read-n-characters-given-read4-ii-call-multiple-times

比较麻烦的写法

The read4 API is already defined for you.
@param buf a list of characters
@return an integer
you can call Reader.read4(buf)
"""
class Solution:
    def __init__(self):
        self.last_buffer = [None] * 4
        self.next_read = 0
        self.count_in_buffer = 0
        
    # @param {char[]} buf destination buffer
    # @param {int} n maximum number of characters to read
    # @return {int} the number of characters read
    
    def read(self, buf, n):
        # Write your code here
        count = self.readBuf(buf, 0, n)
        while count < n:
            cnt = Reader.read4(self.last_buffer)
            self.count_in_buffer += cnt
            if cnt == 0:
                return count
            count += self.readBuf(buf, count, n - count)
        return count
            
    def readBuf(self, buf, i, n):
        count = 0
        while self.count_in_buffer and count < n:
            buf[i] = (self.last_buffer[self.next_read % 4])
            self.next_read = (self.next_read + 1) % 4
            self.count_in_buffer -= 1
            count += 1
            i+=1
        return count