"""
600. Smallest Rectangle Enclosing Black Pixels
https://www.lintcode.com/problem/smallest-rectangle-enclosing-black-pixels/description
九章算法课上的方法

"""
class Solution:
    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    @return: an integer
    """
    def minArea(self, image, x, y):
        # write your code here
        if not image or not image[0]:
            return 0
        n = len(image)
        m = len(image[0])

        left = self.binary_search_first(image, 0, y, self.check_col)
        right = self.binary_search_last(image, y, m - 1, self.check_col)
        up = self.binary_search_first(image, 0, x, self.check_row)
        down = self.binary_search_last(image, x, n - 1, self.check_row)

        print(left, right, up, down)
        return (right - left + 1) * (down - up + 1)

    def binary_search_first(self, image, start, end, check_func):
        while start + 1 < end:
            mid = (start + end) // 2
            if check_func(image, mid):
                end = mid
            else:
                start = mid
        if check_func(image, start):
            return start
        return end

    def binary_search_last(self, image, start, end, check_func):
        while start + 1 < end:
            mid = (start + end) // 2
            if check_func(image, mid):
                start = mid
            else:
                end = mid
        if check_func(image, end):
            return end
        return start

    def check_row(self, image, mid):
        m = len(image[0])
        for i in range(m):
            if image[mid][i] == '1':
                return True
        return False

    def check_col(self, image, mid):
        n = len(image)
        for i in range(n):
            if image[i][mid] == '1':
                return True
        return False
