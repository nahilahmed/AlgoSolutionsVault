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


def find_equilibrium_index(nums):  # O(N)

    prefix_sum = create_prefix_sum(nums)  # O(N)
    for i in range(0, len(nums)):  # O(N)
        if i == 0:
            left_sum = 0
        else:
            left_sum = get_range_sum(prefix_sum, 0, i - 1)  # O(1)

        right_sum = get_range_sum(prefix_sum, i + 1, len(nums) - 1)  # O(1)

        if left_sum == right_sum:
            return (nums[i], i)

    return "No Eq"


def bruteforce_approach(nums):  # O(N2)

    for i in range(0, len(nums)):
        left_sum = 0
        right_sum = 0
        for j in range(0, i):
            left_sum += nums[j]
        for k in range(i + 1, len(nums)):
            right_sum += nums[k]
        if left_sum == right_sum:
            return (nums[i], i)
    return "No Eq"


nums = [1, 7, 3, 6, 5, 6]
nums2 = [1, 2, 4, 5]
print(find_equilibrium_index(nums2))
