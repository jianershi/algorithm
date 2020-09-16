"""
1551. Minimum Operations to Make Array Equal
https://leetcode.com/contest/weekly-contest-202/submissions/detail/381499239/
"""
class Solution:
    def minOperations(self, n: int) -> int:
        arr = []
        for i in range(n):
            arr.append((2*i) + 1)
        target = sum(arr) // len(arr)
        count = 0
        for i in range(n // 2):
            count += target - arr[i]
        return count
