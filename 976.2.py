"""
4Sum II
"""
class Solution:
    """
    @param A: a list
    @param B: a list
    @param C: a list
    @param D: a list
    @return: how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero
    """
    def fourSumCount(self, A, B, C, D):
        # Write your code here
        hash_map = {}
        for i in A:
            for j in B:
                hash_map[i + j] = hash_map.get(i + j, 0) + 1

        count = 0
        for i in C:
            for j in D:
                count += hash_map.get(- (i + j), 0)
        return count

s = Solution()
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

print(s.fourSumCount(A,B,C,D))
