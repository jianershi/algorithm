class Solution:
    """
    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    """
    def longestPalindromeSubseq(self, s):
        # write your code here
        n = len(s)
        start, end = 0, len(s) - 1
        max_length = 0
        while start < end:
            for x in range(end, start, -1):
                if s[start] == s[x]:
                    end = x - 1
                    max_length += 2
                    if end - start == 1:
                        max_length += 1
                    break
            start += 1
        print (max_length)
s = Solution()
# s.longestPalindromeSubseq("asdasdajjdkajwiejladjkahsdjhawiueauwhdjashdjancnkjsahduiawudhajsnhsjahjdhawuahdjshjnzanjcnhjdashuawhdjaksndjkahduwhwauhdai")
s.longestPalindromeSubseq("abkcbcka")
