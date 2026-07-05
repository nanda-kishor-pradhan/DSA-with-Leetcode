# Ques No 409 - Longest Palindrome

# Problem Statement:
# Given a string s which consists of lowercase or uppercase letters, return the length of the longest  that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome.

 

# Example 1:

# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

# Example 2:

# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.


class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = {}
        for i in s:
            seen[i] = seen.get(i,0)+1
        ans = 0
        odd = 0
        for val in seen.values():
            if val % 2 == 0:
                ans+=val
            else:
                ans+=val-1
                odd = 1
        return ans+odd
obj = Solution()
print(obj.longestPalindrome("abccccdd"))