def bubbleSort(array):
    # Write your code here.
    for i in range(len(array)):
        swapped = False
        for j in range(1, len(array) - i):
            if array[j - 1] > array[j]:
                temp = array[j]
                array[j] = array[j - 1]
                array[j - 1] = temp
                swapped = True
        print(array)
        if swapped == False:
            break

    return array


# Time complexity: O(n^2)
array = [1, 2, 3, 4]
bubbleSort(array)
