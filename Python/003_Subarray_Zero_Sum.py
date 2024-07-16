def create_prefix_sum(nums_array): #O(N)   
    prefix_sum = [0] * len(nums_array)
    prefix_sum[0] = nums_array[0]

    for i in range(1,len(nums_array)):
        prefix_sum[i] = prefix_sum[i - 1] + nums_array[i]
    
    return prefix_sum

def get_range_sum(prefix_sum, start, end): #O(1)
    if start == 0:
        return prefix_sum[end]
    return prefix_sum[end] - prefix_sum[start - 1]

def brute_force_approach(nums):
    for i in range(0, len(nums)):
        sum = 0
        sum += nums[i]
        for j in range(i + 1, len(nums)):
            sum = sum + nums[j]
            if sum == 0:
                print(f"Subarray with Sum Zero Index : ({i},{j})")
                subarray = nums[i:j+1]
                print(subarray)


nums = [1, 2, -2, -1, 0, 1, -1]    
brute_force_approach(nums)