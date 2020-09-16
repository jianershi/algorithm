class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """
    def myPow(self, x, n):
        # write your code here
        if n < 0:
            x = 1 / x
            n = -n
        if n == 0:
            return 1


        temp = self.myPow(x, n // 2) #递归深度 log(n), 时间复杂度log(n)
        if n % 2 == 0:
            return temp * temp
        else:
            return temp * temp * x
        
