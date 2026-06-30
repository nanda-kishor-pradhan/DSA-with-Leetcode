# Ques No 567 - Permutation in String 

# Problem statement:
# Given two strings s1 and s2, return true if s2 contains a of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

 

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false




class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        seen = {}
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return False
        for i in s1:
            if i in seen:
                seen[i]+=1
            else:
                seen[i]=1
        window = {}
        for i in range(n1):
            if s2[i] in window:
                window[s2[i]]+=1
            else:
                window[s2[i]]=1
        if seen == window:
            return True
        for i in range(n1,n2):
            if s2[i] in window:
                window[s2[i]]+=1
            else:
                window[s2[i]]=1
            
            left = s2[i-n1]
            window[left]-=1
            if window[left]==0:
                del window[left]
            
            if seen == window:
                return True
        return False
obj = Solution()
print(obj.checkInclusion("ab","eidbaooo"))