"""
method 1:
divide and conquer

idea:
naively distribute k equally in A and B, so k // 2 from A and B each
A[k // 2]
B[k // 2]
say k // 2 > len(A)

A xxxxxxxxx   |
b xxxxxxxxxxxx|xxxxxx

that means the cut in A needs to move left
the cut in b needs to move to the right

so that the count from beginning to cut location still adds up to k
A xxxxxxxxx   |
         ^
b xxxxxxxxxxxx|xxxxxx
                   ^
              i    j
in B we know the number between i and j is bigger than 0-i,
so if we adjust the cut this way, we can make sure number from 0-i in B must
be in the first k smallest number in a combined A and B sorted array

then we only needs to look for
(k - i - 1)th smallest number in A and B[i + 1:]

A xxxxx|xxxxxxxxxx
       i
B xxxxx|xxxxxxxxxx
       j
if both cut are valid
A[i] < B[i]
that means A[0] - A[i] must be in the combined kth smallest.
we need to search A[i:] and B
"""
class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        # write your code here
        n = len(A)
        m = len(B)
        total_length = n + m
        if total_length % 2 == 1: #odd
            return self.find_kth(A, 0 , B, 0, total_length // 2 + 1)
        return (self.find_kth(A, 0, B, 0, total_length // 2) + self.find_kth(A, 0, B, 0, total_length // 2 + 1)) / 2.0

    """
    @param: A: An sorted integer array
    @param: B: An sorted integer array
    @param: A: start_index_A: start searching from the start_index_A
    @param: B: start_index_B: start searching from the start_index_B
    @param: k: kth smallest number from combined sorted list of A[start_index_A: ] and B[start_index_B: ]
    @return: a float
    """
    def find_kth(self, A, start_index_A, B, start_index_B, k) -> float:
        if start_index_A == len(A):
            return B[start_index_B + k - 1]
        if start_index_B == len(B):
            return A[start_index_A + k - 1]
        if k == 1:
            return min(A[start_index_A], B[start_index_B])

        smallest_k_half_in_A = A[start_index_A + k // 2 - 1] if start_index_A + k // 2 - 1 < len(A) else None
        smallest_k_half_in_B = B[start_index_B + k // 2 - 1] if start_index_B + k // 2 - 1 < len(B) else None

        if smallest_k_half_in_B is None or (smallest_k_half_in_A is not None and smallest_k_half_in_A < smallest_k_half_in_B):
            return self.find_kth(A, start_index_A + k // 2, B, start_index_B, k - k // 2)
        return self.find_kth(A, start_index_A, B, start_index_B + k // 2, k - k // 2)
