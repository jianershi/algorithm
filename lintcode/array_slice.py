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
    
    longest_odd_len, odd = find_longest_slice(0, A)
    longest_even_len, even = find_longest_slice(1, A)

    pairs = sorted([odd, even])
    
    if pairs[0][1] < pairs[1][0]:
        return max(longest_odd_len, longest_even_len) + 1
    else:
        return max(pairs[1][1],pairs[0][1]) - pairs[0][0] + 1

def find_longest_slice(starting_index, A):
    n = len(A)
    prev = None
    longest_len = 0
    curr_len = 0
    curr_start = None
    start, end = -1, -1
    for i in range(starting_index, n, 2):
        if prev is None or A[i] != prev:
            curr_start = i
            curr_len = 1
        
        elif A[i] == prev:
            curr_len += 1 
            if curr_len > longest_len:
                start = curr_start
                end = i
                longest_len = curr_len
        prev = A[i]

    return (longest_len, [start, end])
# print(solution([3,2,3,2,3]))
print(solution([1,0,0, 0,1]))