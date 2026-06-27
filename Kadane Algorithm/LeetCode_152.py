# Ques No 53 - Maximum Subarray

# Problem Statement:
# Given an integer array nums, find the with the largest sum, and return its sum.


# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.


class Solutionn:
    def maxProduct(self, nums):
        best = nums[0]
        ans = nums[0]
        minimum = nums[0]
        for i in range(1,len(nums)):
            v1 = nums[i]
            v2 = nums[i]*best
            v3 = nums[i]*minimum

            best = max(v1,v2,v3)
            minimum = min(v1,v2,v3)

            ans = max(ans , best , minimum)
        return ans
obj = Solutionn()
print(obj.maxProduct([2,-5,-2,-4,3]))