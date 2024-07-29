def selection_sort(array):
    for i in range(len(array)):
        min = array[i]
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < min:
                min = array[j]
                min_index = j
        if min_index == i:
            print(array)
            continue
        else:
            array[i], array[min_index] = array[min_index], array[i]
        print(array)
    return array


array = [64, 25, 12, 22, 11]
selection_sort(array)
