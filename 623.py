"""
623. K Edit Distance
https://www.lintcode.com/problem/k-edit-distance/description?_from=ladder&&fromId=106
九章强化班

frist thought:
DP:
same as Edit Distance, but with K
dp[i][j]: how many steps to edit last char i and target's last char j 
dp[i][j] = min(dp[i][j - 1] + 1, dp[i - 1][j] + 1, dp[i - 1][j - 1] + 1, dp[i - 1][j - 1][k] if words[i] == words[j])
do it for all words:

a lot of repeating calculation
abca
abcb
abcd

then abc has to compare with target for all words
->Trie

create a Trie
dp[node][j]: how many steps to edit the prefix represented by this node to target's last char j

answer:
dp[node][j] <= K and node is_word and word in dict


use DFS to avoid create a 2D array
dp[j] for each node

initial condition
dp[""][j] = j #empty string -> prev j's char in target: j
dp[node][0] = len(prefix)

"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, words):
        for word in words:
            p = self.root
            for c in word:
                p.children[c] = p.children.get(c, TrieNode())
                p = p.children[c]
            p.is_word = True
            p.word = word

class Solution:
    """
    @param words: a set of stirngs
    @param target: a target string
    @param k: An integer
    @return: output all the strings that meet the requirements
    """
    def kDistance(self, words, target, k):
        # write your code here
        trie = Trie()
        trie.add(words)

        n = len(target)
        f = [i for i in range(n + 1)] #initial conditon: empty string -> prev j's char in target: j

        results = []
        self.dfs(trie.root, f, n, k, target, results)
        return results

    def dfs(self, root, f, n, k, target, results):
        if f[n] <= k and root.is_word:
            results.append(root.word)
        """
        p (sp)
        |
        c (c)
        |
        p.children[c] (sp c)
        """
        for child in root.children:
            newf = [0] * (n + 1)
            newf[0] = f[0] + 1 #initial condition dp[node][0] = len(prefix)

            for j in range(1, n + 1):
                newf[j] = min(newf[j - 1] + 1, f[j - 1] + 1, f[j] + 1)
                #  
                
                if child == target[j - 1]: #no edit
                    newf[j] = min(newf[j], f[j - 1])

            self.dfs(root.children[child], newf, n, k, target, results)

        