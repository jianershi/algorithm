"""
Rabin-karp
calculate all hash for s and a, any substring of s hash can be calculated in
O(1) from prefix hashes.

   l r
01234567
abcdefgh
say key is def
3-5 def                    31^2 d + 31^1 e + 31^0 f def desired hash value
31^5 a + 31^4 b + 31^3 c + 31^2 d + 31^1 e + 31^0 f a-f in hash of s
31^2 a + 31^1 b + 31^0 c                            a-c in hash of s
----------------------
this part * 31^3
               ^
               length of key

hash_code = (s_hash[r] % MOD - ((s_hash[l - 1]) % MOD * (b_hash[r - l + 1]) % MOD) % MOD)

tatal number of keys = k
total number of characters in s = n
average length of keys = key_length
# of occurances of keys in s: occurance

1 time calculation hash for all s: O(n)
1 time calculation hash for all key: O(k * key_length)
build translation from a->b: O(k)
sort(a) by reverse length: O(klogk)
to search through all keys in s: O(n) * O(k) * O(1)
 - O(n) # of chars
 - O(k) # number of keys
 - O(1) each key search is only O(1) because hash was pre-calculated
once it is found, it takes O(target key_length) to search through char by char
then it takes O(n) to assemble modified s
O(n + k * key_length + k + klogk) + O(n * k * 1) + O(occurance) * O(n)

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
        MOD = 2000000
        translation = self.map_a_to_b(a, b)
        b_hash = self.build_base_hash(len(s), MOD)
        a.sort(key=lambda x: -len(x)) #sort so that longer keys are always replaced first
        a_hash = self.build_key_hash(a, MOD)
        s_hash = self.build_s_hash(s, MOD)
        l = 0
        while l < len(s):
            for i in range(len(a)):
                r = l + len(a[i]) - 1
                #0123456
                #abcdefg
                if r > len(s) - 1: #if right pointer is larger than length of string, continue to next keys
                    continue
                if l < 1: # if left poiters is less than 1, then, it's hash_code doesn't have to be calcuated from it's prefix'es hashcode
                    hash_code = s_hash[r]
                else:
                    hash_code = (s_hash[r] % MOD - ((s_hash[l - 1]) % MOD * (b_hash[r - l + 1]) % MOD) % MOD)
                if hash_code < 0: #add back 1 MOD if previous subtraction ended up negative
                    hash_code += MOD
                if a_hash[a[i]] == hash_code:
                    #check if they actually match
                    if s[l: r + 1] == a[i]:
                        #0123456
                        #abcdefg
                        #
                        s = s[:l] + translation[a[i]] + s[l + len(a[i]):] #modify s
                        l += len(a[i]) - 1 #update left pointer to the desired location -1, with the next l+=1 it will end up in right location
                        break
            l += 1 #update the pointer regardless of found or not found

        return (s)

    """
    @param: a, b a list of keys and their corresponding translations to b
    @return: a dict from a to b
    """
    def map_a_to_b(self, a, b):
        translation = {}
        for key_index in range(len(a)):
            translation[a[key_index]] = b[key_index]
        return translation

    """
    @param: power, 31^0 power 0, 31^1 power 1
    @param: MOD, a large number for MOD operation
    this function returns the nth power of 31 MODded
    """
    def build_base_hash(self, power, MOD):
        #only have to time length
        b_hash = []
        b_hash.append(1)
        base_hash = 1
        for i in range(1, power):
            base_hash = (base_hash * 31) % MOD
            b_hash.append(base_hash)
        return b_hash

    """
    @param: a, key list
    @param: MOD, a large number for MOD operation
    @return: a dict with key and its hash modded
    """
    def build_key_hash(self, a, MOD):
        #calculate hash for keys
        a_hash = {} #key:hashcode
        for key in a:
            key_hash = 0
            for i in range(len(key)):
                #abc
                #012
                #((0*31+a)*31+b)*31+c
                #a*31^2 + 31*b + c
                key_hash = (key_hash * 31 + ord(key[i])) % MOD
            a_hash[key] = key_hash
        return a_hash

    """
    @param: s, original stirng
    @param: MOD, a large number for MOD operation
    @return: a list of hashcode of s
    """
    def build_s_hash(self, s, MOD):
        s_hash = [] #index, it's hashcode from 0-index
        hash_code = 0
        for i in range(len(s)):
            hash_code = (hash_code * 31 + ord(s[i])) % MOD
            s_hash.append(hash_code)
        return s_hash


s = Solution()
A= ["ab","aba"]
B= ["cc","ccc"]
S="ababa"
print(s.stringReplace(A, B, S))
