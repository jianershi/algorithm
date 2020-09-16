class Solution:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """

    """
    thoguht process:
    take the first pattern, supposed it match 0-len(str) characters, then for the remaining characters, matches 2nd thing in the pattern,  continue. if when all pattern are tried but either str is exceeded or none, that means it is not the right dictionary. popping back.
    """
    def wordPatternMatch(self, pattern, str):
        # write your code here
        mapping = {}
        used = set()

        result = self.dfs(pattern, str, mapping, used)
        print(result)
        return result

    def dfs(self, pattern, str, mapping, used):
        print ("pattern: %s, str: %s, mapping: %s, used: %s" % (pattern, str, mapping, used))
        if not pattern:
            return not str

        p = pattern[0]
        if p in mapping:
                match_word = mapping[p]
                if str.startswith(match_word):
                    return self.dfs(pattern[1:], str[len(match_word):], mapping, used)
                else:
                    return False
        for index in range(len(str)):
            word = str[: index + 1]
            if word in used:
                continue
            mapping[p] = word
            used.add(word)
            if self.dfs(pattern[1:], str[index + 1:], mapping, used):
                return True
            del mapping[p]
            # del inverse_mapping[str[: index + 1]]
            used.remove(word)

        return False


def main():
    s = Solution()
    s.wordPatternMatch("ab", "redblue")

if __name__ == "__main__":
    main()
