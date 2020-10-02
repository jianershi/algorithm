"""
415. Valid Palindrome
https://www.lintcode.com/problem/valid-palindrome/description
"""
class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        # write your code here
        # 先processs string to minimal format O(n)
        # 再从中间往两边寻找O(n)
        # 总体时间法度 O(n)
        new_string = self.remove_format(s)
        len_string = len(new_string)

        #异常检测
        if not len_string: return True

        #奇数
        if len_string % 2 == 1:
            for length in range((len_string - 1) // 2 + 1):
                mid = (len_string - 1) // 2
                if new_string[mid + length] != new_string[mid - length]:
                    break
                if length == mid:
                    return True
        #偶数
        else:
            for length in range(len_string // 2):
                mid_left = len_string // 2 -1
                mid_right = len_string // 2
                if new_string[mid_left - length] != new_string[mid_right + length]:
                    break
                if length == mid_left:
                    return True
        return False
    """
    @param s: orinal string
    @return: a string all lower case remove space
    """
    def remove_format(self, s):
        new_string = []
        for char in s:
            if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                new_string.append(char.lower())
            if char in "abcdefghijklmnopqrstuvwxyz0123456789":
                new_string.append(char)
        return ("".join([str(i) for i in new_string]))
        # return new_string
