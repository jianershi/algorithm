"""
656. Multiply Strings

The length of both num1 and num2 is < 110.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

"""
class Solution:
    """
    @param num1: a non-negative integers
    @param num2: a non-negative integers
    @return: return product of num1 and num2
    """
    def multiply(self, num1, num2):
        # write your code here
        num1_lens = len(num1)
        num2_lens = len(num2)
        num3_lens = num1_lens + num2_lens

        num3 = [0] * num3_lens


        for i in range(num1_lens - 1, -1, -1):
            for j in range(num2_lens - 1, -1, -1):
                num3[i + j + 1] +=  (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))

        for i in range(num3_lens - 2, -1, -1):
            num3[i] += num3[i + 1] // 10
            num3[i + 1] %= 10


        #find first none zero location in result array
        while i < num3_lens and num3[i] == 0:
            i += 1

        #when everything is 0
        if i == num3_lens:
            return "0"

        result = ""
        return result.join([chr(x + ord('0')) for x in num3[i:]])
