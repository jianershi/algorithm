"""
1893. the Valid String
https://www.lintcode.com/problem/the-valid-string/description?_from=ladder&&fromId=152
"""
class Solution:
    """
    @param s: a String
    @return: if valid return "YES" else return "NO"
    """
    def isValid(self, s):
        # write your code here
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        
        un_matched_count = 0
        last = None
        for i in range(len(count)):
            if count[i] == 0:
                continue
            if last == None:
                last = count[i]
                continue
            
            if count[i] != last:
                un_matched_count += min(count[i], abs(count[i] - last))
                if un_matched_count > 1:
                    return 'NO'
                    
            last = count[i]
            
        return "YES"