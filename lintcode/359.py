"""
359. makeEquilateralTriangle
https://www.lintcode.com/problem/makeequilateraltriangle/leaderboard

notice u only need to cut *at most* 2 times
"""
class Solution:
    """
    @param lengths: the lengths of sticks at the beginning.
    @return: return the minimum number of cuts.
    """
    def makeEquilateralTriangle(self, lengths):
        # write your code here.
        lengths.sort()
        counters = {}
        n = len(lengths)
        max_count, num = 0, -1
        for w in lengths:
            if max_count == 2:
                if w != num:
                    return 1
                else:
                    return 0
                    
            counters[w] = counters.get(w,0) + 1
            
            if (counters[w] > max_count):
                max_count = counters[w]
                num = w
            
            if w % 2 == 0 and w // 2 in counters:
                return 1

        return 2