import math
# Compare nums[i] with nums[i+1], swap if nums[i+1] < nums[i]
# d
def bubble_sort(nums):
    isSorted = False
    while not isSorted:
        isSorted = True
        for i in range(len(nums) - 1):
            if nums[i+1] < nums[i]:
                isSorted = False
                temp = nums[i]
                nums[i] = nums[i+1]
                nums[i+1] = temp
    return nums
# Iterates from i to to len(nums) and finds the minimum value
# Swap the minimum value with i. Left side[index<i] is now sorted, Right side is not
# Repeat this for every value in the array
# O(n^2)
def selection_sort(nums):
    print(nums)
    for i in range(len(nums)):
        currMinIndex = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[currMinIndex]:
                currMinIndex = j
        temp = nums[i]
        nums[i] = nums[currMinIndex]
        nums[currMinIndex] = temp

    return nums

def insertion_sort(nums):
    for i in range(1, len(nums)):
        j = i
        while j >= 1 and nums[j] < nums[j-1]:
            temp = nums[j]
            nums[j] = nums[j-1]
            nums[j-1] = temp
            j -= 1
        print(nums)
    return nums

# Uses a pivot point
def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums.pop()
    left, right = [], []
    for i in range(len(nums)):
        if nums[i] < pivot:
            left.append(nums[i])
        else:
            right.append(nums[i])
    print(left,pivot,right)
    left = quick_sort(left)
    right = quick_sort(right)
    left.append(pivot)

    left += right
    return left 

def merge_sort(nums):
    if len(nums) == 1:
        return nums
    mid = (0+len(nums))//2
    left = merge_sort(nums[:mid])
    right = merge_sort((nums[mid:]))
    
    output = []
    l,r = 0, 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            output.append(left[l])
            l += 1
        else:
            output.append(right[r])
            r += 1
    if l < len(left):
        output += left[l:]
    elif r < len(right):
        output += right[r:]
    return output
            



def binary_search(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l+r)//2
        if target == nums[mid]:
            return mid
        if target > nums[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return False

# jumps by blockSize M whereby m = math.sqrt(len(nums))
# Keeps jumping, until target is less than the end
def jump_search(nums,target):
    blockSize = int(math.sqrt(len(nums)))
    end = 0
    while nums[min(end,len(nums)-1)] < target and end < len(nums):
        end += blockSize

    for i in range(max(end-blockSize,0), end + 1):
        if i < len(nums) and nums[i] == target:
            return i
    return False
arr = [5,22,4,21,2,5,10,9]
print(arr)
arr = quick_sort(arr.copy())
print(arr)
print(sorted(arr))
print("End of sorting")
print(binary_search(arr, 21))
print(jump_search(arr, 2))
print(jump_search(arr, 21))