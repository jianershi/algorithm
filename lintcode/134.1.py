"""
134. LRU Cache
https://www.lintcode.com/problem/lru-cache/description
"""
class LinkedNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        
class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.capacity = capacity
        self.count = 0
        self.key_to_prev = {}
        self.dummy = LinkedNode(None, None)
        self.tail = self.dummy
        
    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        # write your code here
        if key not in self.key_to_prev:
            return -1
        self.kick_to_back(key)
        return self.tail.val

    def kick_to_back(self, key):
        prev = self.key_to_prev[key]
        curr = prev.next
        if curr == self.tail:
            return
        prev.next = curr.next
        if prev.next:
            self.key_to_prev[prev.next.key] = prev
        self.tail.next = curr
        self.key_to_prev[key] = self.tail
        self.tail = self.tail.next
        self.tail.next = None
        
        
    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        # write your code here
        if key in self.key_to_prev:
            self.kick_to_back(key)
            self.tail.val = value
            return
        self.tail.next = LinkedNode(key, value)
        self.key_to_prev[key] = self.tail
        self.tail = self.tail.next
        self.count += 1
        if self.count > self.capacity:
            del self.key_to_prev[self.dummy.next.key]
            self.dummy = self.dummy.next