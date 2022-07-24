"""
200 · Longest Palindromic Substring
https://www.lintcode.com/problem/200/

"""
class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # write your code here
        # 遍历字符串，作为中点
        # 然后在用子程序以中点开始勋章palidnrome substirng,
        # 全部结束

        #异常检测
        if not s:
            return s
        # if len(s) == 1:
        #     return s

        max_sub = ""
        for index in range(len(s)):
            #check odd
            odd_palindrome = self.find_palindrome_substring(s, index, index)
            # print (odd_palindrome)
            if len(odd_palindrome) > len(max_sub): max_sub = odd_palindrome
            #check even
            even_palindrome = self.find_palindrome_substring(s, index, index+1)
            # print (even_palindrome)
            if len(even_palindrome) > len(max_sub): max_sub = even_palindrome
        return max_sub


    """
    @return: the longest substring around midpoint
    """
    def find_palindrome_substring(self, s, mid_l, mid_r):
        while mid_l >= 0 and mid_r < len(s):
            if s[mid_l] != s[mid_r]:
                break
            mid_l -= 1
            mid_r += 1
        return s[mid_l+1:mid_r]
