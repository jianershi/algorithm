"""
658. Find K Closest Elements
https://leetcode.com/problems/find-k-closest-elements/

->finding the lower boundary of the sliding window where desired results resdies
->numbers between left and right pointers are candidates of *lower bound*
->when l == r-> we have found our lower bound

@vincent_gui listed the following cases:
Assume A[mid] ~ A[mid + k] is sliding window

case 1: x - A[mid] < A[mid + k] - x, need to move window go left
-------x----A[mid]-----------------A[mid + k]----------

case 2: x - A[mid] < A[mid + k] - x, need to move window go left again
-------A[mid]----x-----------------A[mid + k]----------

case 3: x - A[mid] > A[mid + k] - x, need to move window go right
-------A[mid]------------------x---A[mid + k]----------

case 4: x - A[mid] > A[mid + k] - x, need to move window go right
-------A[mid]---------------------A[mid + k]----x------

-------------------------------------------------------
      ^                     | ^
      mid                   | mid + k
      [                     ] <- notice mid + k is outside of the candidate range

so when arr[mid + k] is closer to x,
arr[mid] can never be included in the result array (becasue then the count of numbers between the window is k, including a[mid] will be k + 1)
left = mid + 1

when arr[mid] is closer to x
then arr[mid + k] cannever be in the result array (same reasoning, the sliding window size is k instead of k + 1)
we can also safely discard any *left bound candidate* from [mid + 1:] <- reason being, including mid + 1 will slide the window that covers a[mid +k], which contradicts to the fact that num[mid] is closer to x than num[mid + k], if we were to including num[mid + k], num[mid] must be included, thus contradicts with the assumption
since [mid + 1:] is not a candidate for the left bound
right = mid
"""
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - k
        while l < r:
            mid = (l + r) // 2
            if x - arr[mid] > arr[mid + k] - x:
                l = mid + 1
            else:
                r = mid
            
        return arr[l:l + k]