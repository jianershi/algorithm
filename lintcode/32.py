"""
32. Minimum Window Substring

"""
class Solution:
    """
    @param source : A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """
    def minWindow(self, source , target):
        # write your code here
        freqT = [0] * 256
        target_match = 0
        for c in target:
            freqT[ord(c)] += 1
            if freqT[ord(c)] == 1:
                target_match += 1

        n = len(source)

        right = 0
        freqS = [0] * 256
        source_match = 0
        min_left, min_right = 0, n + 1

        for left in range(n):
            while right < n and source_match < target_match:
                freqS[ord(source[right])] += 1
                if freqS[ord(source[right])] == freqT[ord(source[right])]:
                    source_match += 1 #here
                right += 1
            """
            | abcdefghi | jk
              ^           ^
              l           r
            """
            if source_match == target_match and right - left < min_right - min_left:
                min_left, min_right = left, right

            freqS[ord(source[left])] -= 1
            if freqS[ord(source[left])] == freqT[ord(source[left])] - 1:
                source_match -= 1

        return source[min_left: min_right] if (min_left, min_right) != (0, n + 1) else "" #don't need + 1 because right is already + 1
