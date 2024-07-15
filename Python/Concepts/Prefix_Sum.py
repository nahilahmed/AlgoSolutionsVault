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
