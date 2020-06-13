class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        nums.sort()
        if len(nums) < 2:
            return len(nums)

        # slow_ptr, faster_ptr = 0, 1
        # while slow_ptr < len(nums) and faster_ptr < len(nums):
        #     if nums[slow_ptr] == nums[faster_ptr]:
        #         while nums[slow_ptr] == nums[faster_ptr]:
        #             faster_ptr += 1
        #             if faster_ptr > len(nums) - 1:
        #                 print (nums[0:slow_ptr + 1])
        #                 return slow_ptr + 1
        #         nums[slow_ptr + 1] = nums[faster_ptr]
        #         slow_ptr += 1
        #     else:
        #         slow_ptr += 1
        #         faster_ptr += 1

        # print (nums[0:slow_ptr + 1])
        # return slow_ptr + 1

        """
        这么写思路更加简单。
        首先i是正常遍历的，无论什么情况都到下一个，然后比较i和i-1的大小。假如不同的话，那就是正常。然后把慢的那个pointer指的地方用i指的值覆盖，这表示值要慢pointer经过的地方一定是unique的。要是相同了。慢指针就停了，快指针继续走到下一个不同的地方。然后继续往慢指针存。最后慢指针的index是多少就是有多少个unique number
        """
        num_result = 1
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[num_result] = nums[i]
                num_result += 1
        return num_result
                
