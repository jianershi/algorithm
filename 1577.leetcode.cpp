/**
 * 1577. Number of Ways Where Square of Number Is Equal to Product of Two Numbers
 * https://leetcode.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/
 * two pointers
 */
class Solution {
public:
    int numTriplets(vector<int>& nums1, vector<int>& nums2) {
        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());
        int type1 = countType(nums1, nums2);
        int type2 = countType(nums2, nums1);
        return type1 + type2;
    }
    
    int countType(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size(), m = nums2.size();
        int count = 0;
        for (int i = 0; i < n; ++i) {
            long long t = pow(nums1[i],2), l = 0, r = m - 1;
            while (l < r) {
                while (l < r && (long long) nums2[l] * nums2[r] > t) r--;
                while (l < r && (long long) nums2[l] * nums2[r] < t) l++;
                if (l < r && (long long) nums2[l] * nums2[r] == t) {
                    int len = r - l + 1, num = nums2[l];
                    int countL = 1, countR = 1;
                    while (l < r && nums2[r - 1] == nums2[r]) {
                        r--;
                        countR++;
                    }
                    while (l < r && nums2[l + 1] == nums2[l]) {
                        l++;
                        countL++;
                    }
                    if (l == r && nums2[l] == num) count += len * (len - 1) / 2; //every number is the same
                    else count += countL * countR; //combine left side and right side combination
                    l++;
                    r--;
                }
            }
        }
        return count;
    }
};