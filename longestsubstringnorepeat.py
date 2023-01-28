Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

Solution

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 0
        temp_str = ''
        for i in (s):
            if i not in temp_str:
                temp_str += i
                max_count = max(max_count, len(temp_str))                
            elif i in temp_str:
                temp_str = temp_str[temp_str.index(i)+1:] + i
                max_count = max(max_count, len(temp_str))      
        return (max_count)


