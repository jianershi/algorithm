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
            result[i] = prefix_sum[i] * suffix_sum[i + 1]
            """
            index 0123
                    ^
            str   3841
                    ^
            prefix_sum = [1, 3, 24, 96, 1]
            prefix_sum[2] = s[0] * s[1] = 3 * 8


            index     3210
                        ^
            str[::-1] 1483
                        ^
            prefix_sum of flipped string = [1, 1, 4, 32, 96]
            s[2] = 8
            prefix_sum of flipped string [2] = 4

            postfix_sum = prefix_sum of flipped string[::-1] = [96, 32, 4, 1, 1]
            s[2] = 8
            postfix_sum[2 + 1] = 4
            that's why there is + 1

            """
        return result

    def build_prefix_product(self, nums):
        prefix_product = [None] * (len(nums) + 1)
        prefix_product[0] = 1
        for i in range(1, len(nums) + 1):
            prefix_product[i] = prefix_product[i - 1] * nums[i - 1]

        return prefix_product
