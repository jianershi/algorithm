class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """

    def intersection(self, nums1, nums2):
        nums1.sort()
        result = set()

        for number in nums2:
            if number not in result and self.binary_search(nums1, number):
                result.add(number)
        return list(result)

    def binary_search(self, nums, target):
        if not nums:
            return False

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            else:
                end = mid
        if nums[start] == target:
            return True
        if nums[end] == target:
            return True
        return False

s = Solution()
nums1 = [4,7,9,7,6,7]

nums2 = [5,0,0,6,1,6,2,2,4]

print (s.intersection(nums1, nums2))
