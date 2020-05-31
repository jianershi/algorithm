class Solution:
    """
    @param n: An integer
    @param times: an array of integers
    @return: an integer
    """
    def copyBooksII(self, n, times):
        # write your code here
        if n == 0:
            return 0
        if not times:
            return -1
        if min(times) == 0:
            return 0
        max_time = n // len(times) * max(times) + 1 #everyone read slowest, add 1 because // go lower
        min_time = n // len(times) * min(times) #everyone read fastest

        start, end = min_time, max_time
        while start + 1 < end:
            mid = (start + end) // 2
            if self.books_to_finish_in_timelimit(mid, times) < n:
                start = mid
            else:
                end = mid

        if self.books_to_finish_in_timelimit(start, times) >= n:
            return start
        if self.books_to_finish_in_timelimit(end, times) >= n:
            return end
        return -1

    def books_to_finish_in_timelimit(self, timelimit, times):
        book_count = 0
        for speed in times:
            book_count += timelimit // speed
        return book_count

s = Solution()
n = 4
times = [3, 2, 4]
print (s.copyBooksII(n, times))
