"""
582. Word Break II
https://www.lintcode.com/problem/word-break-ii/my-submissions
memo
"""
class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    def wordBreak(self, s, wordDict):
        # write your code here
        return self.dfs(s, 0, wordDict, {})
        
    def dfs(self, s, index, wordDict, memo):
        if index in memo:
            return memo[index]
            
        paths = []
        n = len(s)
        if index == n:
            memo[index] = []
            return []
            
        if s[index:] in wordDict:
            paths.append(s[index:])
            
        for i in range(index, n):
            prefix = s[index: i + 1]
            if prefix not in wordDict:
                continue
            right_paths = self.dfs(s, i + 1, wordDict, memo)
            
            for path in right_paths:
                paths.append(prefix + " " + path)
                
        
        memo[index] = paths
        return memo[index]