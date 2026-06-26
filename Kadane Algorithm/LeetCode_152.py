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