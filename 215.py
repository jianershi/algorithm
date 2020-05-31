class Solution:
    """
    @param: timestamp: the current timestamp
    @param: event: the string to distinct different event
    @param: rate: the format is [integer]/[s/m/h/d]
    @param: increment: whether we should increase the counter
    @return: True or False to indicate the event is limited or not
    """
    def __init__(self):
        self.log = {} #{event : [] list}


    def isRatelimited(self, timestamp, event, rate, increment):
        # write your code here
        time_range_dict = {
                "s": 1,
                "m": 60,
                "h": 3600,
                "d": 3600 * 24
        }
        # update_rate = int(rate[-3::-1]) * time_range_dict[rate[-1]]
        if event not in self.log:
            if increment:
                self.log[event] = [timestamp]
            return False
        #print (self.log, timestamp, update_rate, timestamp - update_rate)
        index = self.binary_search(self.log[event], 0, len(self.log[event]) - 1, timestamp - time_range_dict[rate[-1]])
        print (self.log, timestamp, timestamp - time_range_dict[rate[-1]], index)
        # print(self.log[event])
        if index!= - 1 and len(self.log[event]) - index >= int(rate[:-2]):
            # print(int(rate[:-2]))
            return True
        if increment:
            self.log[event].append(timestamp)
        return False

    def binary_search(self, nums, start, end, target):
        if not nums:
            return -1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            else:
                end = mid

        if nums[start] > target:
            return start
        if nums[end] > target:
            return end
        if nums[start] != target and nums[end] != target:
            return -1
        while nums[end] == target and end + 1 < len(nums) and nums[end + 1] > target:
            end += 1
        return end - 1



s = Solution()
print(s.isRatelimited(5, "signup", "10/s", True))
print(s.isRatelimited(5, "signup", "10/s", True))
print(s.isRatelimited(8, "signin", "1/m", True))
print(s.isRatelimited(8, "signin", "1/m", True))
print(s.isRatelimited(8, "signin", "5/m", True))
print(s.isRatelimited(8, "signin", "5/m", True))
print(s.isRatelimited(9, "signup", "1/m", True))
print(s.isRatelimited(9, "signin", "1/m", True))
print(s.isRatelimited(10, "signin", "60/s", True))
print(s.isRatelimited(15, "signup", "3/m", True))
print(s.isRatelimited(15, "signup", "3/m", True))
print(s.isRatelimited(20, "signin", "1/m", True))
print(s.isRatelimited(20, "signin", "1/m", True))
print(s.isRatelimited(21, "signin", "10/s", True))
print(s.isRatelimited(22, "signin", "10/s", False))
print(s.isRatelimited(22, "signin", "10/s", False))
print(s.isRatelimited(27, "signup", "60/s", True))
print(s.isRatelimited(27, "signup", "60/s", True))
print(s.isRatelimited(30, "signup", "5/m", False))
print(s.isRatelimited(30, "signup", "5/m", False))
print(s.isRatelimited(30, "signin", "5/m", True))
print(s.isRatelimited(30, "signin", "5/m", True))
print(s.isRatelimited(33, "signup", "10/s", True))
print(s.isRatelimited(38, "signin", "10/s", False))
print(s.isRatelimited(39, "signin", "60/s", True))
print(s.isRatelimited(39, "signin", "60/s", True))
print(s.isRatelimited(40, "signin", "3/m", True))
print(s.isRatelimited(45, "signup", "5/m", True))
print(s.isRatelimited(48, "signin", "1/m", True))
print(s.isRatelimited(48, "signin", "1/m", True))
print(s.isRatelimited(50, "signup", "10/s", True))
print(s.isRatelimited(50, "signup", "10/s", True))
print(s.isRatelimited(50, "signup", "60/s", True))
print(s.isRatelimited(52, "signup", "3/m", True))
print(s.isRatelimited(52, "signup", "3/m", True))
print(s.isRatelimited(53, "signup", "60/s", True))
print(s.isRatelimited(58, "signup", "1/m", False))
print(s.isRatelimited(58, "signup", "1/m", False))
print(s.isRatelimited(62, "signin", "5/m", True))
print(s.isRatelimited(67, "signup", "10/s", False))
print(s.isRatelimited(72, "signin", "1/m", False))
print(s.isRatelimited(74, "signup", "5/m", True))
print(s.isRatelimited(74, "signup", "5/m", True))
print(s.isRatelimited(75, "signin", "5/m", True))
print(s.isRatelimited(80, "signup", "10/s", True))
print(s.isRatelimited(82, "signin", "5/m", True))
print(s.isRatelimited(82, "signin", "5/m", True))
print(s.isRatelimited(86, "signup", "10/s", False))
print(s.isRatelimited(86, "signin", "3/m", True))
print(s.isRatelimited(91, "signin", "10/s", True))
print(s.isRatelimited(91, "signin", "10/s", True))
print(s.isRatelimited(94, "signup", "1/m", True))
print(s.isRatelimited(99, "signin", "3/m", False))
