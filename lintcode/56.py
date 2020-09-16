class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        #遍历一遍，边遍历变查询哈希表，如果余数不再哈希表里面，就把当前值假如哈希表。如果在，就直接返回。这个方法
        #时间复杂度O(n) 空间复杂度O(n)
        hashmap = {} #值, index
        for index, num in enumerate(numbers):
            if target - num in hashmap:
                return [hashmap[target - num], index]
            #如果target - 现在的数不再哈希表里面，就把当前的值假如哈希表
            hashmap[num] = index
        return [-1, -1]
        
        # """
        # 方法2:
        # 先sort 时间复杂度O(nlogn)，如果只需要返回值的话空间复杂度是O(1)，但是这边是需要返回index,这就不是O(1)了
        # 然后2pointers O(n), 空间复杂度 O(1)
        # 合起来时间复杂度O(n+nlogn) = O(nlogn), 空间复杂度如果只返回值的话O(1), 但是这边要返回index所以O(n)
        
            