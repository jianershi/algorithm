"""
array slice
https://leetcode.com/discuss/interview-question/234975/array-slice
"""
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import sys
def solution(A):
    # write your code in Python 3.6
    if not A:
        return 0
    
    n = len(A)
    if n == 1:
        return 1
    
    count = 2
    res = 2
    for i in range(2, n):
        if A[i] == A[i - 2]:
            count += 1
            res = max(res,count)
        else:
            res = max(res,count)
            count = 2
    return max(res, count)
# print(solution([3,2,3,2,3]))
# print(solution([3,2,3,2,3,4,3,2]))
# print(solution([1,0,0, 0,1]))
print(solution([0,0,0]))