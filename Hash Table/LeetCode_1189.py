# Ques No 1189 - Maximum Number of Balloons

# Problem Statement:
# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

# Example 1:

# Input: text = "nlaebolko"
# Output: 1

# Example 2:

# Input: text = "loonbalxballpoon"
# Output: 2


class Solution:
    def Balloons(self,text):
        seen = {'b':0 , 'a':0 , 'l':0 , 'o':0 , 'n':0}
        for i in text:
            if i in seen:
                seen[i]+=1
        
        seen['l'] //= 2
        seen['o'] //= 2
        return min(seen.values())
obj = Solution()
print(obj.Balloons("loonbalxballpoon"))