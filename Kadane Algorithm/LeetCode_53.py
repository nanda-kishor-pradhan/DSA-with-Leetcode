class Solutionn:
    def MaximumSubarray(self, nums):
        best = nums[0]
        ans = nums[0]
        for i in range(1,len(nums)):
            best = max(nums[i],best+nums[i])
            ans = max(best,ans)
        return ans
obj = Solutionn()
print(obj.MaximumSubarray([-2,1,-3,4,-1,2,1,-5,4]))