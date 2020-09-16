"""
Movie Rating

defition:
dp[i][condition] : max sum can get from *previous* ith movies, when choose to SKIP/NOT_SKIP at ith step

function:
dp[i][SKIP] = dp[i - 1][NOT_SKIP]
dp[i][NOT_SKIP] = max(dp[i - 1][SKIP], dp[i - 1][NOT_SKIP]) + nums[i - 1]


initialization:
dp[0][NOT_SKIP] = 0
dp[0][SKIP] = 0

answer:
max(dp[n])

define:
1 not skipping
0 skip
"""
import sys
class Solution:
    def movie_rating(self, ratings):
        if not ratings:
            return 0

        n = len(ratings)

        dp = [[0] * 2 for _ in range(n + 1)]

        dp[0][0] = 0
        dp[0][1] = 0

        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][1] #skipping current step, then previous step cannot be skipped
            dp[i][1] = max(dp[i - 1][0], dp[i - 1][1]) + ratings[i - 1] #not skipping current step, then previous step can either be skipepd or not skipped

        return max(dp[n])

s = Solution()
ratings = [9, -1, -3, 4, 5]
# n = sys.stdin.read().splitlines()
# n = [int(x) for x in n[1:]]
# print (n)
# ratings = n
print(s.movie_rating(ratings))
