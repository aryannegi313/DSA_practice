def two_sum_sorted(numbers, target):
    left = 0
    right = len(numbers) - 1
    while left < right:
        summation = numbers[left] + numbers[right]
        if summation > target:
            right = right - 1
        elif summation < target:
            left = left + 1
        else:
            return [left, right]
    return []
            
    
    
numbers = [2, 7, 11, 15]
target = 18
print(two_sum_sorted(numbers, target))  # [1, 2]