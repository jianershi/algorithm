"""
1850. Pick Apples
https://www.lintcode.com/problem/pick-apples/description

"""
class Solution:
    """
    @param A: a list of integer
    @param K: a integer
    @param L: a integer
    @return: return the maximum number of apples that they can collect.
    """
    def PickApples(self, A, K, L):
        # write your code here
        n = len(A)
        if K + L > n:
            return -1

        max_K_before = self.find_max_before(A, K)
        max_K_after = self.find_max_before(A[::-1], K)[::-1]
        max_L_before = self.find_max_before(A, L)
        max_L_after = self.find_max_before(A[::-1], L)[::-1]


        max_apples = 0
        for div in range(n - 1):
            max_apples = max(max_apples,                                \
                            max_K_before[div] + max_L_after[div + 1],   \
                            max_L_before[div] + max_K_after[div + 1]    \
                        )
        return max_apples

    def find_max_before(self, A, window_size):
        n = len(A)
        max_before = [0] * n
        left = 0
        right = 0
        subarray_sum = 0
        while right < n:
            subarray_sum += A[right]
            if right < window_size - 1:
                max_before[right] = 0
                right += 1
                continue
            if left > 0:
                subarray_sum -= A[left - 1]
            max_before[right] = max(max_before[right - 1], subarray_sum)
            left += 1
            right += 1
        return max_before

s = Solution()
A = [6,1,4,6,3,2,7,4]
K = 3
L = 2
print(s.PickApples(A, K, L))
