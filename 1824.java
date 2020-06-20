public class Solution {
    /**
     * @param s : string s
     * @param minLength : min length for the substring
     * @param maxLength : max length for the substring
     * @param maxUnique : max unique letter allowed in the substring
     * @return: the max occurrences of substring
     */
    public int getMaxOccurrences(String s, int minLength, int maxLength, int maxUnique) {
        // write your code here
        if (s == null || s.length() == 0 || s.length() < minLength) {
            return 0;
        }

        int right = 0;
        int n = s.length();
        char[] strs = s.toCharArray();

        Map<String, Integer> maxOccurance = new HashMap<>();
        Map<Character, Integer> uniqueChar = new HashMap<>();

        for (int left = 0; left < n; ++left) {
            while (right < n && right - left < minLength) {
                uniqueChar.put(strs[right], uniqueChar.getOrDefault(strs[right], 0) + 1);
                ++right;
            }
            if (right - left == minLength) {
                if (uniqueChar.size() <= maxUnique) {
                    String substring = s.substring(left, right);
                    maxOccurance.put(substring, maxOccurance.getOrDefault(substring, 0) + 1);
                }
            }

            uniqueChar.put(strs[left], uniqueChar.get(strs[left]) - 1);

            if (uniqueChar.get(strs[left]) == 0) {
                uniqueChar.remove(strs[left]);
            }

        }
        int maxOccuranceCount = Integer.MIN_VALUE;
        for (Integer value: maxOccurance.values()) {
            maxOccuranceCount = Math.max(maxOccuranceCount, value);
        }
        if (maxOccuranceCount == Integer.MIN_VALUE) {
            return 0;
        } else {
            return maxOccuranceCount;
        }
    }
}
