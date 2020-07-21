"""
1347. Factorial Trailing Zeroes
https://www.lintcode.com/problem/factorial-trailing-zeroes/description?_from=ladder&&fromId=152

这题。。。我没想出来。。
首先只要找prime factor 5,2的pair就可以了。
然后5出现的次数>=2出现的次数。等于说只需要数5出现的次数。。
然后唯一不一样的地方就是有多个5 factorial 的的数字。25 = 5 * 5， 50 = 5 * 5 * 2， 这种。 100 = 5 * 5 * 4 
                                         ^ 第一个5本来就算去了无所谓
                                             ^ 第2个5多出来的可以和其他2配对。等于说每出现5的power就需要多加1. 怎么算多加多少个。不断除5
100//5 + 100//25 + 100//125
     5         5 * 5     5 * 5 * 5 
     1*5       2*5       3*5
                   ^
                   1 additional 5
                                 ^ 1 additional 5

so i only have to find out how many aditional 5 i need to add.

"""
class Solution:
    """
    @param n: a integer
    @return: return a integer
    """
    def trailingZeroes(self, n):
        # write your code here
        # return 0 if n < 5 else self.trailingZeroes(n // 5) + n // 5
        return int(math.sqrt(n // 5)) + n // 5