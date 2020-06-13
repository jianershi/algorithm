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
        self.UF(len(accounts))

        email_to_id = self.build_email_to_id(accounts)

        for email, ids in email_to_id.items():
            main_id = ids[0]
            for id in ids[1:]:
                self.union(id, main_id)

        id_to_email_list = self.build_id_to_email_list(accounts)

        result = []
        for id, emails in id_to_email_list.items():
            line = [accounts[id][0]]
            line.extend(sorted(emails))
            result.append(line)
        return result

    def UF(self, size):
        for i in range(size):
            self.fathers[i] = i

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

    def build_email_to_id(self, accounts):
        email_to_id = {}
        for account_id, account_emails in enumerate(accounts):
            for email in account_emails[1:]:
                email_to_id[email] = email_to_id.get(email, [])
                email_to_id[email].append(account_id)
        return email_to_id

    def build_id_to_email_list(self, accounts):
        id_to_email_list = {}
        for account_id, account_emails in enumerate(accounts):
            main_account_id = self.find(account_id)
            list = id_to_email_list.get(main_account_id, set())
            for email in account_emails[1:]:
                list.add(email)
            id_to_email_list[main_account_id] = list

        return id_to_email_list
        
s = Solution()
accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]

s.accountsMerge(accounts)
