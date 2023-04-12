#  This is 5th leetcode problem

# https://leetcode.com/problems/longest-palindromic-substring/



# Given a string s, return the longest 

# palindromic
 

# substring
#  in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.
# Solution

def longestPalindrome(s: str) -> str:
    res = ''
    res_l = 0
    for i in range(len(s)):
        l,r = i,i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            _len = r - l + 1
            if _len > res_l:
                res_l = _len
                res = s[l:r+1]
            l -= 1
            r += 1

        l,r = i,i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            _len = r - l + 1
            if _len > res_l:
                res_l = _len
                res = s[l:r+1]
            l -= 1
            r += 1
    return res


# This is two pointer approach

# Two cases 1. is odd length 2. even length


# if string is odd, we will get the middle pointer take the case of `cac` here middle pointer is nothing but `a`

# after that we will decrement the l pointer and increment the r pointer with the condition l>=0 here = sign because index starts from 0,4
# and right pointer when it reach len(string) then we compare s[l] == s[r], then we update the maxlenght and thus by result string. here
# length is nothing but  r-l + 1 since index starts from zero it may go negative also which result in wrong answer

# second case only difference is we wont get mid point so take, i, i+1, `caca` take `i` as `a` and `I+1` as `c`


# Brut Force approach, is below
# print all combination of each string, consider like prefix sum, loop again find the string which is reverse of same 
# string find the string with max of the element

l = []
j = 0
k = 0
new = ''
while j < len(s):
    for i in range(len(s)):
        substring = s[j:i + 1]
        if substring:
            l.append(substring)
    j += 1

# l = [s[begin:end+1] for begin in range(len(s)) for end in range(begin, len(s))]    
    
for each in l:
    if each == each[::-1]:
        k =max(k, len(each))
        if len(each) >= k:
            new = each
       
      
#  Ref: https://www.youtube.com/watch?v=ZJUGtWObroc, https://www.youtube.com/watch?v=XYQecbcd6_c
