# DSA_practice
Important DSA concepts and solutions

## Problem rules
- Each Python file implements a separate DSA problem or approach.
- Brute-force versions use nested loops to explore all possibilities.
- Optimized versions use problem-specific tricks like sliding window, prefix sum, complements, and hash maps.
- Return `0` or an empty result when no valid solution exists, depending on the problem.

## Files and Techniques

- `two_sum.py`
  - Problem: Find all pairs of indices whose values add up to `target`.
  - Technique: complement + hashmap.
  - Trick: for each number `x`, check whether `target - x` is already seen.

- `two_sum_bf.py`
  - Problem: Same as `two_sum.py` using brute force.
  - Technique: nested loops.
  - Trick: test every pair once using `i < j`.

- `max_sum_sliding_window.py`
  - Problem: Maximum sum of any contiguous subarray of size `k`.
  - Technique: sliding window.
  - Trick: maintain a running window sum and update by subtracting the leaving element and adding the entering element.

- `max_sum_bf.py`
  - Problem: Same as `max_sum_sliding_window.py` using brute force.
  - Technique: nested loops.
  - Trick: compute each window sum independently from scratch.

- `longest_subarray_with_sum_k.py`
  - Problem: Longest contiguous subarray whose sum equals `k`.
  - Technique: prefix sum + hashmap.
  - Trick: store prefix sums and use `prefix_sum - k` to find earlier matching sum indices.

- `longest_subarray_with_sum_k_bf.py`
  - Problem: Same as `longest_subarray_with_sum_k.py` using brute force.
  - Technique: nested loops.
  - Trick: compute the sum for each candidate subarray and update the maximum length when the sum equals `k`.
