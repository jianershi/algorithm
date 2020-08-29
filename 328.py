"""
328. String Partition
https://www.lintcode.com/problem/string-partition/my-submissions
1. find all indexes of a unique char
2. build max range of unique char
3. sort range
3. merge range
4. got len of range and return
"""
class Solution:
    """
    @param s: a string
    @return:  an array containing the length of each part
    """
    def splitString(self, s):
        # write your code here.
        map = {}
        for i, c in enumerate(s):
            map[c] = map.get(c, [])
            map[c].append(i)


        intermediate = []
        for k,v in map.items():
            intermediate.append([min(v), max(v)])

        intermediate.sort()

        res = []
        for ran in intermediate:
            if (len(res) == 0 or ran[0] > res[-1][1]):
                res.append(ran)
            else:
                res[-1][1] = max(res[-1][1], ran[1])
        return [x[1]-x[0]+1 for x in res]
