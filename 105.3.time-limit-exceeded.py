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

traverse old list and new list and for each random in old node, traverse new list
to find the correct node to attach to the corresponding new node.

this will exceed time limit but space O(1)
"""
class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        new_list_head = self.copy_node(head) #copy node in order, key: node

        self.re_link(new_list_head, head)#relink

        return new_list_head

    def copy_node(self, head):
        if not head:
            return head
        dummy = RandomListNode(None)
        new_p = dummy
        p = head
        while p:
            new_p.next = RandomListNode(p.label)
            new_p = new_p.next
            p = p.next
        return dummy.next

    def re_link(self, new_head, old_head):
        p = new_head
        o_p = old_head
        while p:
            if o_p.random:
                p_seeker = new_head
                while p_seeker:
                    if p_seeker.label == o_p.random.label:
                        break
                    p_seeker = p_seeker.next
                p.random = p_seeker
            p = p.next
            o_p = o_p.next
