# Ques No 383 - Ransom Note 
 
# Problem Statement:
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

 

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        seen , seen1 = {},{}
        for i in ransomNote:
            seen[i] = seen.get(i,0)+1
        for i in magazine:
            seen1[i] = seen1.get(i,0)+1
        for key , val in seen.items():
            if seen1.get(key,0) < val:
                return False
        return True
obj = Solution()
print(obj.canConstruct("aa","ab"))