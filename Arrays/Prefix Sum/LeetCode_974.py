# Ques No 974 -Subarray Sums Divisible by K

# Problem Statement:
# Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

# A subarray is a contiguous part of an array.

 

# Example 1:

# Input: nums = [4,5,0,-2,-3,1], k = 5
# Output: 7
# Explanation: There are 7 subarrays with a sum divisible by k = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

# Example 2:

# Input: nums = [5], k = 9
# Output: 0


class Solution:
    def subarraysDivByK(self, nums,k):
        seen = {0:1}
        sum = 0
        res = 0
        for i in range(len(nums)):
            sum += nums[i]
            rem = sum % k
            if rem < 0:
                rem += k
            if rem in seen:
                res += seen[rem]
            seen[rem] = seen.get(rem,0)+1
        return res
obj = Solution()
print(obj.subarraysDivByK([4,5,0,-2,-3,1],5))