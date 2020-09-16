"""
315. Reformat String
https://www.lintcode.com/problem/reformat-string/description
"""
class Solution:
    """
    @param str: the original string
    @param sublen: an integer array
    @return: the new string
    """
    def reformatString(self, str, sublen):
        # write your code here
        sub = []
        n = len(str)
        i = 0
        j = 0
        while i < n:
            sub.append(str[i:i+sublen[j]])
            i += sublen[j]
            j += 1
            if j == len(sublen):
                break
        # print(sub)
        i = 0
        n = len(sub)
        while 2*i + 1 < n:
            sub[2*i], sub[2*i + 1]= sub[2*i + 1], sub[2*i]
            i += 1
        # print (sub)
        return "".join(sub)
            

s = Solution()
str = "abcdefgh"
sublen = [3, 2, 2, 1]
print(s.reformatString(str, sublen))