"""
1070. Accounts Merge
https://www.lintcode.com/problem/accounts-merge/description
union find?
TLE
"""
class Solution:
    """
    @param accounts: List[List[str]]
    @return: return a List[List[str]]
    """
    def accountsMerge(self, accounts):
        # write your code here
        self.fathers = {}
        dict = {}
        results = {}
        for account_index, account in enumerate(accounts):
            dict[account_index] = account[0]
            self.fathers[account_index] = account_index
            for i in range(1, len(account)):
                if account[i] in self.fathers:
                    self.union(account[i], account_index)
                self.fathers[account[i]] = account_index
        results = []

        for account_index, account_name in dict.items():
            build_tag = []
            new_list = []
            build_tag.append(account_name)
            for id in self.find_all(account_index):
                new_list.append(id)
            if new_list == []:
                continue
            build_tag.extend(sorted(new_list))
            results.append(build_tag)
        return results

    def union(self, a,b):
        a_father = self.find(a)
        b_father = self.find(b)
        if a_father == b_father:
            return
        self.fathers[a_father] = b_father

    def find(self, x):
        if self.fathers[x] == x:
            return x
        self.fathers[x] = self.find(self.fathers[x])
        return self.fathers[x]

    def find_all(self, x):
        list = []
        for id in self.fathers:
            if self.find(id) == x and id != x and not str(id).isdigit():
                list.append(id)

        return list

s = Solution()
accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]

s.accountsMerge(accounts)
