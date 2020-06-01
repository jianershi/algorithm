"""
105. Copy List with Random Pointer
"""
"""
Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

create new list in order
then traverse both list at the same time and find random key and reattach.
"""
class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        new_list_head, new_list_map = self.copy_node(head) #copy node in order, key: node

        self.re_link(new_list_head, head, new_list_map)#relink

        return new_list_head

    def copy_node(self, head):
        if not head:
            return head
        new_map = {}
        dummy = RandomListNode(None)
        new_p = dummy
        p = head
        while p:
            new_p.next = RandomListNode(p.label)
            new_map[p.label] = new_p.next
            new_p = new_p.next
            p = p.next
        return dummy.next, new_map

    def re_link(self, new_head, old_head, new_map):
        p = new_head
        o_p = old_head
        while p:
            if o_p.random:
                p.random = new_map[o_p.random.label]
            p = p.next
            o_p = o_p.next
