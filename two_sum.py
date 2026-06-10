def two_sum(nums, target):
    map = {}
    res = []
    for i in range(len(nums)):
        if target - nums[i] in map.keys():
            res.append((i, map.get(target - nums[i])))
        else:
            map[nums[i]] = i
    
    return res            
    
# Example
nums = [2, 11, 7, 15, 1, 8, 3, 6]
target = 9
print(two_sum(nums, target))  # [0, 2]