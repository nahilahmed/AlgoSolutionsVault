
# Daily Log: Learning Prefix Sum (July 15, 2024)

## Concepts Covered:

**1. Introduction to Prefix Sum:**
   - A prefix sum array is used to store the cumulative sum of elements in an array up to a certain index.
   - It allows for efficient calculation of the sum of any subarray in constant time.

**2. Constructing a Prefix Sum Array:**
   - Given an array `arr`, the prefix sum array `prefix` is constructed as follows:
     - `prefix[0] = arr[0]`
     - For each index `i` from 1 to `n-1`, `prefix[i] = prefix[i-1] + arr[i]`

**3. Using Prefix Sum Array for Range Sum Queries:**
   - To find the sum of elements from index `i` to `j` in the original array, use:
     - `sum(i, j) = prefix[j] - prefix[i-1]`
     - If `i` is 0, `sum(0, j) = prefix[j]`

## Example Problem:

**Given an array `arr = [1, 2, 3, 4, 5]`, construct the prefix sum array and find the sum of elements from index 1 to 3.**

### Solution:

1. **Construct the Prefix Sum Array:**
   - Initialize `prefix[0] = arr[0] = 1`
   - For `i = 1`, `prefix[1] = prefix[0] + arr[1] = 1 + 2 = 3`
   - For `i = 2`, `prefix[2] = prefix[1] + arr[2] = 3 + 3 = 6`
   - For `i = 3`, `prefix[3] = prefix[2] + arr[3] = 6 + 4 = 10`
   - For `i = 4`, `prefix[4] = prefix[3] + arr[4] = 10 + 5 = 15`

   The prefix sum array is `[1, 3, 6, 10, 15]`.

2. **Find the Sum of Elements from Index 1 to 3:**
   - Use the formula: `sum(1, 3) = prefix[3] - prefix[0] = 10 - 1 = 9`

### Python Code Example:

```python
def construct_prefix_sum(arr):
    prefix_sum = [0] * len(arr)
    prefix_sum[0] = arr[0]
    for i in range(1, len(arr)):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i]
    return prefix_sum

def range_sum(prefix_sum, i, j):
    if i == 0:
        return prefix_sum[j]
    return prefix_sum[j] - prefix_sum[i - 1]

# Example usage
arr = [1, 2, 3, 4, 5]
prefix_sum = construct_prefix_sum(arr)
print("Prefix Sum Array:", prefix_sum)
print("Sum of elements from index 1 to 3:", range_sum(prefix_sum, 1, 3))
```

**Output:**
```
Prefix Sum Array: [1, 3, 6, 10, 15]
Sum of elements from index 1 to 3: 9
```

## Summary:

Today, we covered the basics of the prefix sum data structure, including its construction and usage for efficient range sum queries. We also went through an example problem to illustrate these concepts in practice. This foundational knowledge will be useful for solving more complex problems involving cumulative sums and range queries.
