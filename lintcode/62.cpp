/**
 * 62. Search in Rotated Sorted Array
 * https://www.lintcode.com/problem/search-in-rotated-sorted-array/description
 *
 * 33. Search in Rotated Sorted Array
 * https://leetcode.com/problems/search-in-rotated-sorted-array/
 */
class Solution {
public:
    /**
     * @param A: an integer rotated sorted array
     * @param target: an integer to be searched
     * @return: an integer
     */
    int search(vector<int> &A, int target) {
        // write your code here
        int n = A.size();
        if (n == 0) return -1;
        int start = 0, end = n - 1;
        while (start + 1 < end) {
            int mid = start + (end - start) / 2;
            if (A[mid] >= A[start]) {
                if (A[start] <= target && target <= A[mid])
                    end = mid;
                else
                    start = mid;
            } else {
                if (A[mid] < target && target < A[start])
                    start = mid;
                else
                    end = mid;
            }
        }
        if (A[start] == target) return start;
        if (A[end] == target) return end;
        return -1;
    }
};