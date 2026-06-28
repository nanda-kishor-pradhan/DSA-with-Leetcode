# Ques No 1749 - Maximum Absolute Sum of Any Subarray

# Problem Statement:
# You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).

# Return the maximum absolute sum of any (possibly empty) subarray of nums.

# Note that abs(x) is defined as follows:

#     If x is a negative integer, then abs(x) = -x.
#     If x is a non-negative integer, then abs(x) = x.

 

# Example 1:

# Input: nums = [1,-3,2,3,-4]
# Output: 5
# Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.

# Example 2:

# Input: nums = [2,-5,1,-4,3,-2]
# Output: 8
# Explanation: The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8) = 8.



class Solution:
    def maxAbsoluteSum(self, nums):
        maxBest = nums[0]
        maxAns = nums[0]
        minAns = nums[0]
        minBest = nums[0]
        
        for i in range(1,len(nums)):
            maxBest = max(nums[i],maxBest+nums[i])
            maxAns = max(maxAns , maxBest)

            minBest = min(nums[i],nums[i]+minBest)
            minAns = min(minAns , minBest)

            
        return max(abs(minAns),abs(maxAns))
obj = Solution()
print(obj.maxAbsoluteSum([2,-5,1,-4,3,-2]))