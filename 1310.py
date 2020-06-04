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
            result[i] = prefix_sum[i] * suffix_sum[i + 1]

        return result

    def build_prefix_product(self, nums):
        prefix_product = [None] * (len(nums) + 1)
        prefix_product[0] = 1
        for i in range(1, len(nums) + 1):
            prefix_product[i] = prefix_product[i - 1] * nums[i - 1]

        return prefix_product
        
