# Ques No 20 - Valid Parentheses

# Problem Statement:
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.

 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

# Example 5:



class Solution:
    def isValid(self , s):
        stk = []
        pairs = {')':'(','}':'{',']':'['}
        for i in s:
            if i in '({[':
                stk.append(i)
            else:
                if not stk or stk[-1] != pairs[i]:
                    return False
                stk.pop()
        return len(stk) == 0
obj = Solution()
print(obj.isValid("([])"))