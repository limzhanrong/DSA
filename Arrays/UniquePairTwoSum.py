def uniquePairTwoSum(nums, target):
    pool = set()
    used = set()

    for n in nums:
        if target-n in pool:
            used.add((n,target-n))
        else:
            pool.add(n)
    return len(used)