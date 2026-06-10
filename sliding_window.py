def max_sum_subarray_of_size_k(arr,k):
    addition = sum(arr[:k])
    max = addition

    for l in range(len(arr)-k):
        addition = addition - arr[l] + arr[l+k]
        if addition > max:
            max = addition
    return max

arr = [2, 1, 5, 1, 3, 2]
k = 3
print(max_sum_subarray_of_size_k(arr, k))  # 9


