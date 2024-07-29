def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
        print(array)
    return array


array = [8, 5, 2, 9, 6, 3]
insertion_sort(array)
