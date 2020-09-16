import random
class Solution:
    """
    @param {int} n a positive integer
    @param {int} k a positive integer
    @return {Solution} a Solution object
    """
    @classmethod
    def create(cls, n, k):
        # Write your code here
        return cls(n, k)

    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.used_location = set() #save a list of locations on the ring that is already used
        self.machine_location = [] #[(location, machine_id)] this list is always sorted
        
    """
    Time Complexity O(nlogn), mainly because of keep machine_location sorted
    @param: machine_id: An integer
    @return: a list of shard ids
    """
    def addMachine(self, machine_id):
        # write your code here
        new_locations = []
        while len(new_locations) < self.k:
            rand_num = random.randint(0, self.n - 1)
            if rand_num not in self.used_location:
                self.used_location.add(rand_num)
                self.machine_location.append((rand_num, machine_id))
                self.machine_location.sort()
                new_locations.append(rand_num)
        return new_locations

    """
    Time complexity O(logn)
    @param: hashcode: An integer
    @return: A machine id
    """
    def getMachineIdByHashCode(self, hashcode):
        # write your code here
        # self.machine_location.sort() #O(nlogn)
        # self.quick_sort(self.machine_location, 0, len(self.machine_location) - 1)
        # key_list = [x[0] for x in self.machine_location]
        next_machine_index = self.binary_search(self.machine_location, 0, len(self.machine_location) - 1, hashcode) #o(logn)

        if next_machine_index == -1:
            next_machine_index = 0
        return self.machine_location[next_machine_index][1]

    """
    return index in the orginal array where first number > target
    @param: nums: (location, machine_id)
    @param: start: start index in array
    @param: end: index in array
    @target: target
    @return: index of first number which is > target, return -1 if not found
    """
    def binary_search(self, nums, start, end, target):
        if not nums:
            return -1
        while start + 1 < end:
            mid = (start + end) // 2
            if target < nums[mid][0]:
                end = mid
            else:
                start = mid
        if nums[start][0] >= target:
            return start
        if nums[end][0] >= target:
            return end
        return -1

    #use quick select algorithm. will take O(n)
    def quick_select(self, nums, target):
        #change to quick select, pivot may not be in the list
        print ("quickselect, list: %s, target: %d" % (list, target))
        start, end = 0, len(nums) - 1
        left, right = start, end
        while left <= right:
            while left <= right and nums[left] < target:
                left += 1
            while left <= right and nums[right] > target:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        print ("left: %d, right: %d" % (left, right))
        print ("list: %s" % nums)

        if left < len(nums) and nums[left] > target:
            return left
        return -1

    def quick_sort(self, nums, start, end):
        #change to quick select, pivot may not be in the list
        if start >= end:
            return
        left, right = start, end
        pivot = nums[(left + right) // 2][0]
        while left <= right:
            while left <= right and nums[left][0] < pivot:
                left += 1
            while left <= right and nums[right][0] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        self.quick_sort(nums, start, right)
        self.quick_sort(nums, left, end)


def main():
    s = Solution.create(100, 3)
#     print(s.addMachine(1))
#     print(s.getMachineIdByHashCode(4))
#     print(s.addMachine(2))
#     print(s.getMachineIdByHashCode(61))
#     print(s.getMachineIdByHashCode(91))
    # print(s.create(10, 5))
    # print(s.addMachine(1))
    # print(s.getMachineIdByHashCode(4))
    # print(s.addMachine(2))
    # print(s.getMachineIdByHashCode(0))
    # create(100, 3)
    print(s.addMachine(1))
    print(s.getMachineIdByHashCode(4))
    print(s.addMachine(2))
    print(s.getMachineIdByHashCode(61))
    print(s.getMachineIdByHashCode(91))


if __name__ == "__main__":
    main()
