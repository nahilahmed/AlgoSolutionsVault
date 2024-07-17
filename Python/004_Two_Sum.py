def brute_force_approach(nums, target): #O(N2)
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if (nums[i] + nums[j]) == target:
                return (i,j)
    return -1

def better_approach(nums, target):
    values = {}
    for i in range(len(nums)):
        if nums[i] not in values:
            values[nums[i]] = i

    
    for i in range(len(nums)):
        complement_val = target - nums[i]
        if complement_val in values and values[complement_val] != i:
            return (i, values[complement_val])
    
    return -1

        

    

nums = [3,3]
target = 6
print(better_approach(nums, target))