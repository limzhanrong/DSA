import math
class Solution:
    def maxSubArray(self, nums):
        maxSum = -float('inf')
        i = 0
        while(i < len(nums)):
            currSum = nums[i]
            j= i + 1
            if currSum > maxSum:
                    maxSum = currSum
            while currSum >= 0 and j < len(nums):
                currSum += nums[j]
                if currSum > maxSum:
                    maxSum = currSum
                j += 1
            i = j
            
        return maxSum
solution = Solution()
print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

for i in range(5):
    print(i)
    i += 1