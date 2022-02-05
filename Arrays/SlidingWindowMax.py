from collections import deque

# 1
# The idea is to pop and remove all idexes in deque that has lesser value than right pointer while q is not empty
# Every iteration will push into the end of the deque.


# 2
# The most left sided of the deque will be the largest. 
# The elements after the most left sided deque will be higher index AND smaller than the left sided.

# 3
# When the left pointer has become higher than the most left-sided deque index, pop and remove it.
class Solution:
    def slidingWindowMax(self, nums, k):
        output = []
        q = deque()
        l = r = 0

        while(r < len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            print(q)
            if l > q[0]:
                q.popleft()
            
            if r+1 >= k:
                l += 1
                output.append(nums[q[0]])
            r+=1
        return output

solution = Solution()
print(solution.slidingWindowMax([1,3,-1,-3,5,3,6,7],3))