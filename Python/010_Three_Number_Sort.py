# Three Number Sort

# You're given an array of integers and another array of three distinct integers. The first array is guaranteed to only contain integers that are in the second array, and the second array represents a desired order for the integers in the first array. For example, a second array of [x, y, z] represents a desired order of [x, x, ..., x, y, y, ..., y, z, z, ..., z] in the first array.

# Write a function that sorts the first array according to the desired order in the second array.

# The function should perform this in place (i.e., it should mutate the input array), and it shouldn't use any auxiliary space (i.e., it should run with constant space:
# 𝑂
# (
# 1
# )
# O(1) space).

# Note that the desired order won't necessarily be ascending or descending and that the first array won't necessarily contain all three integers found in the second array—it might only contain one or two.


def solution(array, order):
    freq_dict = {}
    for i in range(len(array)):
        if array[i] not in freq_dict:
            freq_dict[array[i]] = 1
        else:
            freq_dict[array[i]] += 1

    print(freq_dict)

    array_ptr = 0
    for i in range(len(order)):
        freq_item = freq_dict[order[i]]
        print(f"Freq Item: {freq_item}")
        for _ in range(0, freq_item):
            array[array_ptr] = order[i]
            array_ptr += 1
        print(array)


def optimized_solution(array, order):
    array_ptr = 0
    for i in range(len(order)):
        val = order[i]
        for j in range(len(array)):
            if array[j] == val:
                array[j], array[array_ptr] = array[array_ptr], array[j]
                array_ptr += 1
        print(array)


array = [1, 0, 1, -1, 1, 0, -1]
order = [0, 1, -1]

optimized_solution(array, order)
