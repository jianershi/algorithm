"""
robin karp:
abcdefgh, find string def
we only need to calculate a hash for def, that kaes O(K)
abcdefgh
---
abcdefgh
 ---
we only have to check the hash kth len's at a time, the hash can be culated in O(1) time
hash(bcd) = hash(abc) * 31 + e - 31^4 * a

it will take O(n) to check all the hash agaist the target hash.
for those rare cases where hashes clides, check letter by letter O(k)
total time O(n + k)
"""
class Solution:
    """
    @param: source: A source string
    @param: target: A target string
    @return: An integer as index
    """
    def strStr2(self, source, target):
        # write your code here
        if source is None or target is None:
            return -1
        if not target:
            return 0
        if not source:
            return -1

        BASE = 2000000
        k = len(target) #3

        highest_power = 1
        for i in range(len(target)):
            highest_power = (highest_power * 31) % BASE

        #abc
        #012 = (a31^2+b*31 + c)
        #31^3=  1*31^31^31
        hash_target = 0
        for i in range(len(target)):
            hash_target = (hash_target * 31 + ord(target[i])) % BASE

        hash_code = 0
        #0123456
        #abcdefg     7
        #efg         3
        for i in range(len(source)):
            #add next char
            hash_code = (hash_code * 31 + ord(source[i])) % BASE

            #a*31^3 + b*31*2+ c*31  +d
            #abcd
            #0123

            if i >= k:
                hash_code = (hash_code - highest_power * ord(source[i - k])) % BASE
            if hash_code < 0:
                hash_code += BASE

            #match
            if hash_code == hash_target:
                match = True
                for j in range(len(target)):
                    if source[i - k + 1 + j] != target[j]:
                        match = False
                        break
                if match:
                    return i - k + 1
        return -1

s = Solution()
source = ""
target = ""
print(s.strStr2(source, target))
