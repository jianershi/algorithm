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

naive way.
find all the random link
copy node by next
then relink random link
"""


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        random_map = self.find_link(head) # map is {label: random label}

        new_list_head, new_list_map = self.copy_node(head) #copy node in order, key: node

        self.re_link(new_list_head, random_map, new_list_map)#relink

        return new_list_head

    def find_link(self, head):
        random_map = {}
        p = head
        while p:
            random_map[p.label] = p.random
            p = p.next
        return random_map

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

    def re_link(self, new_list_head, random_map, new_map):
        p = new_list_head
        while p:
            if random_map[p.label]:
                p.random = new_map[random_map[p.label].label]
            p = p.next
