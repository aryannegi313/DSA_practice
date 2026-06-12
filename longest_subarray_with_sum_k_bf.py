def longest_subarray_sum_k_bruteforce(arr, k):
    """Return the length of the longest contiguous subarray with sum equal to k using brute force."""
    max_length = 0
    n = len(arr)
    for start in range(n):
        current_sum = 0
        for end in range(start, n):
            current_sum += arr[end]
            if current_sum == k:
                max_length = max(max_length, end - start + 1)
    return max_length


if __name__ == "__main__":
    arr = [1, -1, 5, -2, 3, 4, 6, 7, -3, -4]
    k = 3
    print(longest_subarray_sum_k_bruteforce(arr, k))  # 4
