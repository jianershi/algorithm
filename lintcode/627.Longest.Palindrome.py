class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """

    """
    按最大到小排序，排序完成以后只插入偶数，插入完以后插入最大的奇数
    """
    def longestPalindrome(self, s):
        # write your code here
        dict = {}
        # count = 0
        # {dict[char]:dict[char] + 1 for char in s if dict[char] else dict[char]:1}
        length = 0
        print(s)
        for char in s:
            dict[char] =0
        print(dict)
        for char in s:
            dict[char] += 1
        print(dict)

        max_odd = 0
        for (char,count) in dict.items():
            if count % 2 == 0:
                length += count
            else:
                if count > max_odd:
                    max_odd = count

        return length+max_odd

def main():
    s = Solution()
    print(s.longestPalindrome("NTrQdQGgwtxqRTSBOitAXUkwGLgUHtQOmYMwZlUxqZysKpZxRoehgirdMUgy"))

if __name__ == "__main__":
    main()
