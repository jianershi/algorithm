"""
4Sum II
TLE
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
        hash_map1 = {}
        for i in A:
            for j in B:
                hash_map1[i + j] = hash_map1.get(i + j, 0) + 1

        hash_map2 = {}
        for i in C:
            for j in D:
                hash_map2[i + j] = hash_map2.get(i + j, 0) + 1

        count = 0
        for key1, count1 in hash_map1.items():
            for key2, count2 in hash_map2.items():
                if key1 + key2 == 0:
                    count += count1 * count2

        return count

s = Solution()
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

print(s.fourSumCount(A,B,C,D))
