def create_prefix_sum(nums_array): #O(N) 
    if len(nums_array) == 0:
        return []
    prefix_sum = [0] * len(nums_array)
    prefix_sum[0] = nums_array[0]

    for i in range(1,len(nums_array)):
        prefix_sum[i] = prefix_sum[i - 1] + nums_array[i]
    
    return prefix_sum

def get_range_sum(prefix_sum, start, end): #O(1)
    if start == 0:
        return prefix_sum[end]
    return prefix_sum[end] - prefix_sum[start - 1]

def brute_force_approach(nums): #O(N2)
    for i in range(0, len(nums)):
        sum = 0
        for j in range(i, len(nums)):
            sum = sum + nums[j]
            if sum == 0:
                print(f"Subarray with Sum Zero Index : ({i},{j})")
                subarray = nums[i:j+1]
                print(subarray)

def prefix_sum_approach(nums):
    prefix_sum = create_prefix_sum(nums) #O(N)
    prefix_sum_map = {}
    for i in range(0, len(prefix_sum)): #O(N)
        if prefix_sum[i] not in prefix_sum_map:
            prefix_sum_map[prefix_sum[i]] = 1
        else:
            prefix_sum_map[prefix_sum[i]]+=1 

    freq_count = 0
    for key, val in prefix_sum_map.items(): #O(N)
        if val > 1:
            freq_count += (val * (val - 1)) / 2
        if key == 0:
            freq_count += val
    return freq_count

def prefix_sum_approach_2(nums):
    prefix_sum_map = {}
    current_sum = 0
    freq_count = 0

    for num in nums:
        current_sum += num
        
        # If current_sum is zero, we found a subarray
        if current_sum == 0:
            freq_count += 1
        
        # If current_sum is found in the map, it means there are subarrays with zero sum
        if current_sum in prefix_sum_map:
            freq_count += prefix_sum_map[current_sum]
        
        # Update the map with the current_sum
        if current_sum in prefix_sum_map:
            prefix_sum_map[current_sum] += 1
        else:
            prefix_sum_map[current_sum] = 1
    
    return freq_count


# Test cases with expected frequency counts
test_cases = [
    ([1, 2, -2, -1, 0, 1, -1], 9),  # Original case
    ([1, 2, 3, 4, 5], 0),           # No subarray sums to zero
    ([1, -1, 1, -1, 1, -1], 9),     # Multiple subarrays sum to zero
    ([0, 0, 0, 0], 10),             # All elements are zero
    ([], 0),                        # Empty array
    ([0], 1),                       # Single element zero
    ([5], 0),                       # Single element non-zero
    ([-1, 1, -1, 1], 4),            # Alternating positive and negative
    ([1, 1, -1, -1, 1, 1], 5),      # Mix of positive and negative with zero sum subarrays
]

# Testing the function
for i, (test_case, expected) in enumerate(test_cases):
    result = prefix_sum_approach(test_case)
    print(f"Test Case {i+1}: {test_case} -> Frequency Count: {result} (Expected: {expected})")