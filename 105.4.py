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
"""
"""
method by Roger:
source: https://www.jiuzhang.com/solution/copy-list-with-random-pointer/#tag-other-lang-java
O(1) space complexity
+---+ indicate random link

        +--+
src:    1->2->3


step1: copy node
        +------+
src:    1->1'->2->2'->3->3'


step2: copy random link
        +------+
src:    1->1'->2->2'->3->3'
           +------+


step3: split two lists
        +--+
src:    1->2->3

        +---+
dst:    1'->2'->3'
"""

class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        if not head:
            return head

        self.copy_node(head)
        self.copy_random_link(head)
        new_head = self.split_two_list(head)

        return new_head

    def copy_node(self, head):
        p = head
        while p:
            new_p = RandomListNode(p.label)
            new_p.next = p.next
            p.next = new_p
            p = p.next.next

    def copy_random_link(self, head):
        p = head
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next

    def split_two_list(self, head):
        dummy = RandomListNode(None)
        tail = dummy
        o_p = head
        while o_p:
            tail.next = o_p.next
            o_p.next = o_p.next.next
            o_p = o_p.next
            tail = tail.next
        return dummy.next
