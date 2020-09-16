"""
1524. Number of Sub-arrays With Odd Sum
https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/

dp[i][0] : # of subarrays that *end in ith position* that has even sum
dp[i][1] : # of subarrays that *end in ith position* that has odd sum

if nums[i - 1] % 2 == odd:
    dp[i][1] = dp[i - 1][0] + 1
    dp[i][0] = dp[i - 1]
    
else:
    dp[i][0] = dp[i - 1][0] + 1
    dp[i][1] = dp[i - 1][1]
    
answer:
sum(dp[x][1]) sum all the subarrays that ending in xth position that has odd sum

"""
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        if not arr:
            return 0
        n = len(arr)
        dp = [[0] * 2 for _ in range(n + 1)]
        for i in range(1, n + 1):
            if arr[i - 1] % 2 == 1:
                dp[i][1] = dp[i - 1][0] + 1
                dp[i][0] = dp[i - 1][1]
            else:
                dp[i][0] = dp[i - 1][0] + 1
                dp[i][1] = dp[i - 1][1]
        
        return sum([x[1] for x in dp]) % 1000000007