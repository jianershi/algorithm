"""
the problem will be to find the longest substring in S that's in A.
then replace with B

idea 1:
say A is of length k
sort(A) by reverse length O(klogk)
check if A exist in S (each takes O(n))
then replace it roughly O(1) each
so total O(klogk) + O(n)*k

"""
class Solution:
    """
    @param a: The A array
    @param b: The B array
    @param s: The S string
    @return: The answer
    """
    def stringReplace(self, a, b, s):
        # Write your code here
        key_pairs = list(zip(a,b))
        key_pairs.sort(key = lambda x: len(x[0]), reverse=True)
        i = 0
        while i < len(s):
            for key, replacement in key_pairs:
                if s[i:i + len(key)] == key:
                    s = s[:i] + replacement + s[i + len(key):]
                    i += len(key) - 1
                    break
            i += 1
        return s

s = Solution()
A = ["cd","dab","zbc"]
B = ["cc","aaa","ddc"]
S = "cdab"
print(s.stringReplace(A, B, S))
