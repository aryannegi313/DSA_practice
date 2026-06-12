def longest_subarray_sum_k(arr, k):
    """Return the length of the longest contiguous subarray with sum equal to k.

    If no contiguous subarray sums to k, return 0.
    """
    prefix_sum_map = {0: -1}  # Initialize with sum 0 at index -1
    prefix_sum = 0
    max_length = 0
    for i, num in enumerate(arr):
        prefix_sum += num
        diff = prefix_sum - k
        if diff in prefix_sum_map.keys():
            max_length = max(max_length, i - prefix_sum_map.get(diff))
        if prefix_sum not in prefix_sum_map.keys():
            prefix_sum_map[prefix_sum] = i

    return max_length


# Example
arr = [1, -1, 5, -2, 3, 4, 6, 7, -3, -4]
k = 3
print(longest_subarray_sum_k(arr, k))  # 4