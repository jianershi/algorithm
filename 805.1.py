"""
805. Maximum Association Set
https://www.lintcode.com/problem/maximum-association-set/description

Example 1:
	Input:  ListA = ["abc","abc","abc"], ListB = ["bcd","acd","def"]
	Output:  ["abc","acd","bcd","def"]
	Explanation:
	abc is associated with bcd, acd, dfe, so the largest set is the set of all books

easier method. build list of children after wards.
"""
class Solution:
    """
    @param ListA: The relation between ListB's books
    @param ListB: The relation between ListA's books
    @return: The answer
    """
    def maximumAssociationSet(self, ListA, ListB):
        # Write your code here
        n = len(ListA)
        if len(ListB) != n:
            return -1

        self.father = {}

        for i in range(n):
            if ListA[i] not in self.father:
                self.father[ListA[i]] = ListA[i]
            if ListB[i] not in self.father:
                self.father[ListB[i]] = ListB[i]
            self.union(ListA[i], ListB[i])

        children = {} #root_father and a set of its children
        for key in self.father:
            root_id = self.find(key)
            children[root_id] = children.get(root_id, set())
            children[root_id].add(key)

        max_set = set()
        for root_father, child_list in children.items():
            if len(child_list) > len(max_set):
                max_set = child_list
        return list(max_set)



    def union(self, a, b):
        a_father = self.find(a)
        b_father = self.find(b)
        if a_father == b_father:
            return

        self.father[a_father] = b_father

    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]
