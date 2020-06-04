"""
1310. Product of Array Except Self

"""
class Solution:
    """
    @param nums: an array of integers
    @return: the product of all the elements of nums except nums[i].
    """
    def productExceptSelf(self, nums):
        # write your code here
        prefix_sum = self.build_prefix_product(nums)
        suffix_sum = self.build_prefix_product(nums[::-1])[::-1]

        result = [0] * len(nums)
        for i in range(len(result)):
            if i == 0:
                result[i] = suffix_sum[i + 1]
                continue
            if i == len(result) - 1:
                result[i] = prefix_sum[i - 1]
                continue
            result[i] = prefix_sum[i - 1] * suffix_sum[i + 1]
            
        return result

    """
    does include itself. so prefix_product[i] include everything form 0-i
    """
    def build_prefix_product(self, nums):
        prefix_product = [None] * (len(nums))
        prefix_product[0] = nums[0]
        for i in range(1, len(nums)):
            prefix_product[i] = prefix_product[i - 1] * nums[i]

        return prefix_product
