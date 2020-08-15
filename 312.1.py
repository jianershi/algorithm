"""
312. 牛牌
312. Bull Cards
https://www.lintcode.com/problem/bull-cards/description
TLE
"""
class Solution:
    """
    @param n: the number 
    @param m: the number of cards in hand
    @return: the number of different types of cards
    """
    def bullCards(self, n, m):
        # Write your code here.
        MOD = 1000000007
        self.count = 0
        self.dfs(n, m, [0] * n, [4] * n, set())
        return self.count % MOD
        
    def dfs(self, n, m, path, cards, visited):
        if m == 0:
            self.count += 1
            return
        
        for i in range(m):
            for j, card in enumerate(cards):
                if card > 0:
                    cards[j] -= 1
                    path[j] += 1
                    if tuple(path) not in visited:
                        visited.add(tuple(path))
                        self.dfs(n, m - 1, path, cards, visited)
                    path[j] -= 1
                    cards[j] += 1
            
s = Solution()
n = 4
m = 2
print(s.bullCards(n, m))