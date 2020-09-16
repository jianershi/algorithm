/**
* 1371. Find the Longest Substring Containing Vowels in Even Counts
* https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/
* 
* idea: using bitmask to mark status
* each bit 0 represent even appearance, 1 odd appeareance
* 
* for current char in the string s[i], only need to check if exact bit map exist before.
* because 0->even 1->odd, odd + odd = 0 even
* nowCount = 01100 a,e,i,o,u = Even,Odd,Odd,Even,Even
* then, to find the longest substring, need to find the earliest apperance of Even, Odd, Odd, Even, Even of position x, then anything from x + 1 to i must be even.
*
* used string instead of vector
*/

class Solution {
public:
    int findTheLongestSubstring(string s) {
        string vowels = {'a', 'e', 'i', 'o', 'u'};
        int n = s.size(), max_len = 0;
        unordered_map<int, int> prefixSum = {{0, -1}};
        int nowCount = 0;
        for (int i = 0; i < n; ++i) {
            int shift = vowels.find(s[i]);
            if (shift != std::string::npos)
                nowCount = nowCount ^ 1 << shift;
            
            if (prefixSum.count(nowCount)) max_len = max(max_len, i - prefixSum[nowCount]);
            else prefixSum[nowCount] = i; 
            
        }
        
        return max_len;
    }
};