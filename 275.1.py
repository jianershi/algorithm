"""
275. Moving Shed
https://www.lintcode.com/problem/moving-shed/description?_from=contest&&fromId=94

"""
class Solution:
    """
    @param stops: An array represents where each car stops.
    @param k: The number of cars should be covered.
    @return: return the minimum length of the shed that meets the requirements.
    """
    def calculate(self, stops, k):
        # write your code here
        if not stops or len(stops) < 2 or k > len(stops):
            return 0

        stops = sorted(stops)
        n = len(stops)


        if k == n:
            return stops[n - 1] - stops[0] + 1

        shed = 0
        l = 0
        r = k

        """
        shed 的大小。必须是 stops[0] ～ stops[k] 的距离 - 1， 也就是 stops[k] - stops[0] + 1 - 1 = stops[k] - stops[0].
        原因是 
        [1,3,6,7,8]
        e.x. k = 2

        index   0   1       2 3
        pos   0 1 2 3 4 5 6 7 8
                x   x     x x x
                |___| 如果初始化成 stops[0] ~ stops[k - 1]的距离
                  |___| 挂了
                |_______| 正确初始化
                  |_______| 不会挂
        """
        while r < n:
            shed = max(shed, stops[r] - stops[l])
            l += 1
            r += 1

        return shed