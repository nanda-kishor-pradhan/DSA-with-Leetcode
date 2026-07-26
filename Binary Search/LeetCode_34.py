# Ques NO 34 - Find first and last position of element in Sorted Array

# Problem Statement:
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]

from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low , high= 0 , len(nums)-1
        first , last = -1 , -1
        
        while low <= high:
            guess = (low+high)//2
            if nums[guess] < target:
                low = guess+1
            elif nums[guess] > target:
                high = guess-1
            else:
                first = guess
                high = guess - 1
        
        low , high = 0 , len(nums)-1
        while low <= high:
            guess = (low+high)//2
            if nums[guess] < target:
                low = guess+1
            elif nums[guess] > target:
                high = guess-1
            else:
                last = guess
                low = guess+1
        return [first,last]

obj = Solution()
print(obj.searchRange([5,7,7,8,8,10],8))