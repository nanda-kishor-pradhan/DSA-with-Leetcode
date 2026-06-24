# Ques No 796 - Rotate String

# Problem Statement:
# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

# A shift on s consists of moving the leftmost character of s to the rightmost position.

#     For example, if s = "abcde", then it will be "bcdea" after one shift.

 

# Example 1:

# Input: s = "abcde", goal = "cdeab"
# Output: true


class Solution:
    def rotateString(self,s,goal):
        if len(s) != len(goal):
            return False
        else:
            str = s + s
            if goal in str:
                return True
            return False
        
obj = Solution()
print(obj.rotateString("abcde","bcdea"))