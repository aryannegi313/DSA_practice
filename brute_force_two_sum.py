def two_sum_bruteforce(nums, target):
    res = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                res.append((i, j))
    return res


# Example
nums = [2, 11, 7, 15, 1, 8, 3, 6]
target = 9
print(two_sum_bruteforce(nums, target))  # [(0, 2)]
