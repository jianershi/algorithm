"""
method 2:
using a new sequence to track the smallest number of LSI for a given length i
g[i] means for any LISs of length i - 1, g[i] represents the index of smallest ending number of that LIS sequence in the original input array. 
to maintain g:
Find **first** number in g so that nums[g[j]] > nums[i], then replace j with i. If such number does not exist, append j at the end of g
i.e. always maintaining an ascending sorted array when inserting, instead of strictly inserting.
    1) instead of inserting number, it is inserting index of the number in the original array
    2) instead of inserting a smaller number, it is overwriting the next bigger number in g
    3) if it is bigger than all the numbers in g, it appends at the end
=>
2) will ensure for a given lengh i, g[i] is the smallest number.
this array's final length is equal to the length of the longest increasing subsequence

this will result in a strictly sorted array of increasing value but recorded in their indices in original array, which allows binary search on O(logn) on new insertion into g
time complexity: O(nlogn) to traverse through the orinal array

list prev record the parents of each nums[i] when g[i] is updated. if it is added in the front of g[i], that means the number is smaller than all numbers that have seen, so it has no parents, parents = None, otherwise, parents = inserting_point - 1

result: len(g)

index 0 1 2 3 4 5
nums [5,4,1,2,3,0]
g    [0] <-index of 5
prev [None] <- no parents
g    [1] <-index of 4
prev [None, None] <- no parents
g    [2] <- index of 1
prev [None, None, None]
g    [2, 3] <- index of 1,2
prev [None, None, None, 2] <- 2 has parent 1
g    [2, 3, 4] <- index of 1,2,3
prev [None, None, None, 2, 3] < - 3 has parent 2
g    [5, 3, 4] <- index of 0,2,3
prev [None, None, None, 2, 3, None] < - 0 is the smallest number, so it has no parent

"""
class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        g = []
        prev = []
        for i in range(len(nums)):
            index_to_insert_or_replace = self.binary_search(nums, g, nums[i]) #O(logn)
            if index_to_insert_or_replace < len(g):
                g[index_to_insert_or_replace] = i
            else:
                g.append(i)
            if index_to_insert_or_replace - 1 >= 0:
                prev.append(g[index_to_insert_or_replace - 1])
            else:
                prev.append(None)
        
        self.print_parents(prev, nums, g)
        print ("g: %s" % g)
        print ("prev: %s" % prev)
        return len(g)
    
    
    def print_parents(self, prev, nums, LIS_sequence):
        if not LIS_sequence:
            return
        index = LIS_sequence[-1]
        result = []
        while index:
            result.append(nums[index])
            index = prev[index]
        result.reverse()
        print ("one of the LSI: %s" % result)
    
    """
    @return: index of the next bigger number in LIS_sequence that needs to be replaced
            return len(LIS_sequence) if no number in the sequence is larger than target. as the new largest number,
            it needs to be appended in the end of LIS_sequence
    """
    def binary_search(self, nums, LIS_sequence, target):
        if not nums:
            return -1
        start, end = 0, len(LIS_sequence) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[LIS_sequence[mid]] < target:
                start = mid
            else:
                end = mid
        if 0 <= start < len(LIS_sequence):
            if nums[LIS_sequence[start]] >= target:
                return start
        if 0 <= end < len(LIS_sequence):
            if nums[LIS_sequence[end]] >= target:
                return end
        return len(LIS_sequence)
