"""
1396. Set Union

https://www.lintcode.com/problem/set-union/

Input :list = [[1,2,3],[3,9,7],[4,5,10]]
Output:2 .
Explanation:There are 2 sets of [1,2,3,9,7] and [4,5,10] left.

for each set: enumerarte, 0, 1, 2 as it's id
build numbers_to_id 3: 0, 1
union id 0 and 1
then rebuild the list,
get main_id then, then attach all the rest to the list

"""
class Solution:
    """
    @param sets: Initial set list
    @return: The final number of sets
    """
    def setUnion(self, sets):
        # Write your code here
        self.father = {}
        count = 0

        for i in range(len(sets)):
            self.father[i] = i
            count += 1

        nums_to_id = self.build_nums_to_id(sets)

        for num, ids in nums_to_id.items():
            main_id = ids[0] #may have to change if it has duplicates
            for id in ids:
                if self.union(main_id, id):
                    count -= 1
        return count

    def union(self, a, b):
        a_father = self.find(a)
        b_father = self.find(b)

        if a_father == b_father:
            return False

        self.father[a_father] = b_father
        return True

    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]

    def build_nums_to_id(self, sets):
        nums_to_id = {}
        for set_id, nums in enumerate(sets):
            for num in nums:
                nums_to_id[num] = nums_to_id.get(num, [])
                nums_to_id[num].append(set_id)
        return nums_to_id
