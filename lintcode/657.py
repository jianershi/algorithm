"""
657. Insert Delete GetRandom O(1)
https://www.lintcode.com/problem/insert-delete-getrandom-o1/description

380. Insert Delete GetRandom O(1)
https://leetcode.com/problems/insert-delete-getrandom-o1/
"""

import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mem = []
        self.val_to_index = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.val_to_index:
            return False
        self.mem.append(val)
        self.val_to_index[val] = len(self.mem) - 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.val_to_index:
            return False
        
        idx = self.val_to_index[val]
        self.mem[idx], self.mem[-1] = self.mem[-1], self.mem[idx]
        self.val_to_index[self.mem[idx]] = idx
        self.mem.pop()
        del self.val_to_index[val] #this line has to be at the end, in the case that the element popped is the last element
        return True
    
    """
    this works too, but a bit more cumbersome 
    """
    # def remove(self, val: int) -> bool:
    #     """
    #     Removes a value from the set. Returns true if the set contained the specified element.
    #     """
    #     if val not in self.val_to_index:
    #         return False
        
    #     idx = self.val_to_index[val]
    #     del self.val_to_index[val]
    #     self.mem[idx], self.mem[-1] = self.mem[-1], self.mem[idx]
    #     self.mem.pop()
        
    #     if len(self.mem) > 0 and idx < len(self.mem):
    #         self.val_to_index[self.mem[idx]] = idx
        
    #     return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.mem[random.randint(0, len(self.mem) - 1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()