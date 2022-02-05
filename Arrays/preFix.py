class Solution:
    # 238. Product of Array Except Self

    def productExceptSelf(self, nums):
        output = [1] * len(nums)
        for i in range(1, len(nums)):
            if i == 0:
                output[i] = nums[i-1]
            else:
                output[i] = output[i-1] * nums[i-1]
        for i in range(len(nums) - 2,-1,-1):
            nums[i] = nums[i+1] * nums[i]
        for i in range(len(nums) - 1):
            output[i] *= nums[i+1]
        return output