"""
134. LRU Cache
https://www.lintcode.com/problem/lru-cache/description
"""
class LinkedNode:
    def __init__(self, key = None, val = None):
        self.key = key
        self.val = val
        self.next = None
        
class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.key2prev = {}
        self.dummy = LinkedNode()
        self.tail = self.dummy
        self.capacity = capacity
        
    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        # write your code here
        if key not in self.key2prev:
            return -1
        self.kickToBack(key)
        return self.tail.val
            

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        # write your code here
        if key in self.key2prev:
            self.kickToBack(key)
            self.tail.val = value
        else:
            self.tail.next = LinkedNode(key, value)
            self.key2prev[key] = self.tail
            self.tail = self.tail.next
            if len(self.key2prev) > self.capacity:
                self.dummy = self.dummy.next
                del self.key2prev[self.dummy.key]
            
    def kickToBack(self, key):
        prev = self.key2prev[key]
        op = prev.next
        if op == self.tail:
            return
        nt = op.next
        self.tail.next = op
        op.next = None
        self.key2prev[key] = self.tail
        self.tail = self.tail.next
        self.key2prev[nt.key] = prev
        prev.next = nt
        