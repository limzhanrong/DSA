class Solution:
    # Leetcode 416. Partition Equal Subset Sum
 
    def canPartition(self, nums):
        totalSum = sum(nums)
        if totalSum % 2 != 0:
            return False
        targetSum = totalSum/2
        sums = {0}
        for num in nums:
            temp = 0
            for key in sums.copy():
                temp = key + num
                if temp not in sums:
                    sums.add(temp)
                if targetSum in sums:
                    return True
        return False

    def canPartitionRecursion(self, nums):
        totalSum = sum(nums)
        if totalSum % 2 != 0:
            return False
        targetSum = totalSum//2
        memo = set()
        
        def dfs(inputSum, index):
            print(inputSum,memo)
            if inputSum == 0:
                return True
            if inputSum in memo or inputSum < 0:
                print('false')
                return False
            memo.add(inputSum)
#             If targetSum - nums[i] doesn't work, move to next index and become targetSum - nums[i+1]
            for i in range(index, len(nums)):
                boolean = dfs(inputSum - nums[i], i+1)
                if boolean is True:
                    return True
            
        return dfs(targetSum, 0)

solution = Solution()
nums = [1,5,11,5]
print(solution.canPartition([1,5,11,5]))
print(solution.canPartitionRecursion([1,5,11,5]))
# print(nums[1:])