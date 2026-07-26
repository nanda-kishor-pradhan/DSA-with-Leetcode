# Ques No 852 - Peak Index in a Mountain Array

# Problem Statement:
# You are given an integer mountain array arr of length n where the values increase to a peak element and then decrease.

# Return the index of the peak element.

# Your task is to solve it in O(log(n)) time complexity.

 

# Example 1:

# Input: arr = [0,1,0]

# Output: 1

# Example 2:

# Input: arr = [0,2,1,0]

# Output: 1

# Example 3:

# Input: arr = [0,10,5,2]

# Output: 1


from typing import List
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low , high = 0 , len(arr)-1
        while low< high:
            guess = (low+high)//2
            if arr[guess] > arr[guess+1]:
                high = guess
            else:
                low = guess+1
        return low
obj = Solution()
print(obj.peakIndexInMountainArray([0,1,0]))