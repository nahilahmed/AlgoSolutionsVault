## https://leetcode.com/problems/squares-of-a-sorted-array/solutions/

# Square of each number is positive or 0 which means we don't have to care about negative or positive for original numbers. We can foucs on only numbers even if numbers are negative. For example, 4 for -4 or 1 for -1

# Numbers at edge of array will produce bigger number because input array is sorted and we only focus on numbers. In this case, A number at index 0 or index 4 will produce the biggest square number.


def sorted_squared_array_2(array):

    left_pointer = 0
    right_pointer = len(array) - 1

    # squared_array = [i * i for i in array]
    answer_array = [0 for i in range(len(array))]

    i = len(array) - 1

    while left_pointer < right_pointer and i >= 0:
        if abs(array[left_pointer]) > abs(array[right_pointer]):
            answer_array[i] = array[left_pointer] * array[left_pointer]
            left_pointer += 1
        else:
            answer_array[i] = array[right_pointer] * array[right_pointer]
            right_pointer -= 1
        i -= 1
        print(answer_array)

    return answer_array


array = [-7, -3, 2, 3, 11]
print(sorted_squared_array_2(array))
