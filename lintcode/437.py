class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copyBooks(self, pages, k):
        # write your code here
        if not pages:
            return 0
        start, end = max(pages), sum(pages)
        while start + 1 < end:

            mid = (start + end) // 2
            if self.copiers_needed(pages, mid) > k:
                start = mid
            else:
                end = mid
        if self.copiers_needed(pages, start) <= k:
            return start
        if self.copiers_needed(pages, end) <= k:
            return end
        return -1

    def copiers_needed(self, pages, timelimit):
        head_count = 1
        pages_on_hand = 0
        for page in pages:
            if pages_on_hand + page > timelimit:
                head_count += 1
                pages_on_hand = 0
            pages_on_hand += page
        return head_count
