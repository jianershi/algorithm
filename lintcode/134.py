"""
134. LRU Cache
https://www.lintcode.com/problem/lru-cache/description

整体思路：
首先数据结构需要不断删除然后添加到末尾。并且需要有序。用linkedlist比较适合增加删除操作。但是删除本身如果要能在O(1)时间内实现还需要hashmap辅助，用于记录需要删除节点的前面的节点。
"""
class LinkedNode:
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next
        
class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.key_to_prev_node = {}
        self.dummy = LinkedNode()
        self.tail = self.dummy
        self.capacity = capacity

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        # write your code here
        if key not in self.key_to_prev_node:
            return -1
        prev_node = self.key_to_prev_node[key]
        node = prev_node.next
        self.kick_to_back(prev_node)
        return node.value


    def kick_to_back(self, prev_node):
        current_node = prev_node.next
        if current_node == self.tail:
            return
        self.key_to_prev_node[current_node.next.key] = prev_node
        self.key_to_prev_node[current_node.key] = self.tail
        
        prev_node.next = current_node.next
        self.tail.next = current_node
        self.tail = current_node
        self.tail.next = None
        
        
    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        # write your code here
        if key in self.key_to_prev_node:
            prev_node = self.key_to_prev_node[key]
            prev_node.next.value = value
            self.kick_to_back(prev_node)
        else:
            self.key_to_prev_node[key] = self.tail
            self.tail.next = LinkedNode(key, value)
            self.tail = self.tail.next
            if len(self.key_to_prev_node) > self.capacity:
                self.remove_oldest_node()
            
    
    def remove_oldest_node(self):
        if not self.dummy.next:
            return
        head = self.dummy.next
        if not head.next:
            self.dummy.next = None
            self.tail = self.dummy
        else:
            self.key_to_prev_node[head.next.key] = self.dummy
            self.dummy.next = head.next
        del self.key_to_prev_node[head.key]
        
        
