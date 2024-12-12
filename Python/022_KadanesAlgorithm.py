import sys

def create_prefix_sum(nums_array):  # O(N)
    prefix_sum = [0] * len(nums_array)
    prefix_sum[0] = nums_array[0]

    for i in range(1, len(nums_array)):
        prefix_sum[i] = prefix_sum[i - 1] + nums_array[i]

    return prefix_sum

def get_range_sum(prefix_sum, start, end):  # O(1)
    if start == 0:
        return prefix_sum[end]
    return prefix_sum[end] - prefix_sum[start - 1]

def max_subarray(nums):
    # Placeholder for your solution
    if len(nums) == 1:
        return nums[0]
    max_val = -sys.maxsize - 1 # maximum sum
    cummulative_sum = create_prefix_sum(nums)
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            range_value = get_range_sum(cummulative_sum, i, j)
            if max_val <= range_value:
                max_val = range_value
    return max_val

if __name__ == "__main__":
    # Example test cases
    test_cases = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),  # Expected: 6
        ([1], 1),                              # Expected: 1
        ([5, 4, -1, 7, 8], 23),                # Expected: 23
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        print(f"Test case {i}:")
        print(f"Input: {nums}")
        print(f"Expected Output: {expected}")
        print("Your Output:", max_subarray(nums))
        print("-" * 30)