def max_sum_subarray_of_size_k_bruteforce(arr, k):
    """Return the maximum sum of any contiguous subarray of size k using brute-force."""
    if k > len(arr) or k <= 0:
        return 0

    max_sum = float('-inf')
    for start in range(len(arr) - k + 1):
        current_sum = 0
        for j in range(start, start + k):
            current_sum += arr[j]
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum


if __name__ == "__main__":
    arr = [2, 1, 5, 1, 3, 2]
    k = 3
    print(max_sum_subarray_of_size_k_bruteforce(arr, k))  # 9
