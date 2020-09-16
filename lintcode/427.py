class Solution:
    """
    @param n: n pairs
    @return: All combinations of well-formed parentheses
    """
    def generateParenthesis(self, n):
        # write your code here
        paths = []
        self.dfs(n * 2, 0, [], paths)
        print (paths)


    def dfs(self, n, sum, path, paths):
        if sum < 0 or sum > n:
            return
        if n == 0 and sum == 0:
            paths.append("".join(path))
            return
        path.append("(")
        self.dfs(n - 1, sum + 1, path, paths)
        path.pop()
        path.append(")")
        self.dfs(n - 1, sum - 1, path, paths)
        path.pop()

s = Solution()
s.generateParenthesis(3)
