# Ques No 525 - Contiguous Array

# Problem Statement:
# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 

# Example 1:

# Input: nums = [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

# Example 2:

# Input: nums = [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

# Example 3:

# Input: nums = [0,1,1,1,1,1,0,0,0]
# Output: 6
# Explanation: [1,1,1,0,0,0] is the longest contiguous subarray with equal number of 0 and 1.


class Solution:
    def ContiguousArray(self,nums):
        zero , one , res = 0,0,0
        seen = {}
        for i in range(len(nums)):
            if nums[i] == 0:
                zero +=1 
            else:
                one+=1
            diff = zero - one
            if diff == 0:
                res = max(res , i+1)
            if diff not in seen:
                seen[diff] = i
            else:
                indx = seen[diff]
                length = i - indx
                res = max(res,length)
        return res
obj = Solution()
print(obj.ContiguousArray([0,1,1,1,1,1,0,0,0]))