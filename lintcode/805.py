"""
805. Maximum Association Set
https://www.lintcode.com/problem/maximum-association-set/description

Example 1:
	Input:  ListA = ["abc","abc","abc"], ListB = ["bcd","acd","def"]
	Output:  ["abc","acd","bcd","def"]
	Explanation:
	abc is associated with bcd, acd, dfe, so the largest set is the set of all books

whenever union, each father node maintain a list of all childrens under the same union.
when union, then update the list in father. then in order to print out the largest. i need to know
which father has the largest amount of children. but then, i do not know other father's data until union
some may never union. so i still ned to scan through all the fathers to find out the father with
most children.

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
        self.children = {}

        for i in range(n):
            if ListA[i] not in self.father:
                self.father[ListA[i]] = ListA[i]
                self.children[ListA[i]] = self.children.get(ListA[i], set())
                self.children[ListA[i]].add(ListA[i])
            if ListB[i] not in self.father:
                self.father[ListB[i]] = ListB[i]
                self.children[ListB[i]] = self.children.get(ListB[i], set())
                self.children[ListB[i]].add(ListB[i])
            self.union(ListA[i], ListB[i])

        max_set = set()
        for father in self.father:
            if len(self.children[father]) > len(max_set):
                max_set = self.children[father]
        return list(max_set)

    def union(self, a, b):
        a_father = self.find(a)
        b_father = self.find(b)
        if a_father == b_father:
            return

        self.father[a_father] = b_father
        for child in self.children[a_father]:
            self.children[b_father] = self.children.get(b_father, set())
            self.children[b_father].add(child)

    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]
