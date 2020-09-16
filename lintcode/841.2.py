"""
the problem will be to find the longest substring in S that's in A.
then replace with B

idea1:
check if A exist in S by iterate through all chars in s for all char in key in each key

tatal number of keys = k
total number of characters in s = n
average length of keys = key_length
# of occurances of keys in s: occurance

sort(a) by reverse length: O(klogk)
O(n) * O(k) * O(key_length)
- O(n) each char in s
- O(k) # of keys
- O(key_length) #average key_length per key

once it is found, it takes O(target key_length) to search through char by char
then it takes O(n) to assemble modified s

overall O(klogk) + O(n * k * key_length) + O(occurance) * O(n)


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
        replacements = {a[i]:b[i] for i in range(len(a))}
        a.sort(key = lambda x: -len(x))
        i = 0
        while i < len(s):
            for key in a:
                if s[i:i + len(key)] == key:
                    s = s[:i] + replacements[key] + s[i + len(key):]
                    i += len(key) - 1
                    break
            i += 1
        return s

s = Solution()
A = ["cd","dab","zbc"]
B = ["cc","aaa","ddc"]
S = "cdab"
print(s.stringReplace(A, B, S))
