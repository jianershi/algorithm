"""
1305. Integer to English Words
https://www.lintcode.com/problem/integer-to-english-words/leaderboard
"""
class Solution:
    """
    @param num: a non-negative integer
    @return: english words representation
    """
    def numberToWords(self, num):
        # Write your code here
        res = ""
        if num == 0:
            return "Zero"
            
        thousands = ["Billion", "Million", "Thousand"]
        n = 1000000000
        for i in range(3):
            if num // n:
                res += self.convertHundred(num // n) + " " + thousands[i]
                num %= n
            n //= 1000
        res += self.convertHundred(num)
        
        return res[1:]
            
    def convertHundred(self, num):
        underTwenty = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fiftenn", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        res = ""
        if num >= 100:
            res += " " + underTwenty[num // 100] + " " + "Hundred"
            num %= 100
        if num >= 20:
            res += " " + tens[num // 10]
            num %= 10
        if num != 0:
            res += " " + underTwenty[num]
        return res
            
