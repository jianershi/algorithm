"""
1507. Shortest Subarray with Sum at Least K

binary search according to result. intead of finding Shortest Subarray with Sum at Least K.
See if I can find a subarray of maximum lenth mid, so that its sum >= k.
if able, shorten the length see if i can still find such subarray.
if not, then there must not exist a shortest subarray < mid. so increase the subarray length.

be aware, it is not equivalent to: find a there exist a subarray of length mid so that its sum >=k.
because numbers can be negative in the array.

[1,3,5, -10]. a length of 4 array does not exist for sum > 5. but length 3 does exist.

binary search O(logn)

then how to find if there exist such subarray.

problem: is there a subarray of maximum length mid so that its sum >= k

xxxxxxxxxxxxxx
        i    j
we know index wise: j - i + 1 <= mid
then i only need to find at least 1 of such subarray inside i - j:
i can normally do it in n time.
but i can also just find the minimum prefix sum inside i-j. because
to find out if there exist one subarray so that if A[j] - prefix_sum() >= k
i only need to find minimum of all prefix_sum between i and j.
using heap.

i can do it in O(nlogn) time. n positions to search, log(n) for inserting o(1) for peeking

overall O(nlogn*logn) time complexity
"""
import heapq
class Solution:
    """
    @param A: the array
    @param K: sum
    @return: the length
    """
    def shortestSubarray(self, A, K):
        # Write your code here.
        start = 0
        end = len(A)

        while start + 1 < end:
            mid = (start + end) // 2
            if self.is_valid(A, K, mid):
                end = mid
            else:
                start = mid
        if self.is_valid(A, K, start):
            return start
        if self.is_valid(A, K, end):
            return end
        return -1

    def is_valid(self, A, k, mid):
        prefix_sum = [(0, -1)] #prefix_sum, index
        sum = 0
        for j in range(len(A)):
            sum += A[j]
            while prefix_sum and j - prefix_sum[0][1] > mid: #instead of j - i + 1 because i have to initalize (0, -1) in order for 1st prefix_sum to make sense
                heapq.heappop(prefix_sum)
            if prefix_sum and sum - prefix_sum[0][0] >= k:
                return True
            heapq.heappush(prefix_sum, (sum, j))

        return False

s = Solution()
A = [2, -1 , 2]
K = 3
print(s.shortestSubarray(A, K))
