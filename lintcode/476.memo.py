import sys
class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def stoneGame(self, A):
        # write your code here
        if not A:
            return 0
        memo = [[sys.maxsize] * len(A) for _ in range(len(A))]
        return (self.memo_search(A, 0, len(A) - 1, memo))

    """
    return minimum cost for range A[start: end + 1]
    """
    def memo_search(self, nums, start, end, memo):
        if memo[start][end] != sys.maxsize:
            return memo[start][end]

        if start >= end:
            return 0

        current_step_cost = sum(nums[start: end + 1])
        min_cost = sys.maxsize
        for k in range(start, end):
            left_min_cost = self.memo_search(nums, start, k, memo)
            right_min_cost = self.memo_search(nums, k + 1, end, memo)
            min_cost = min(min_cost, left_min_cost + right_min_cost + current_step_cost)
        memo[start][end] = min_cost
        return min_cost

A = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]


s = Solution()
print(s.stoneGame(A))
