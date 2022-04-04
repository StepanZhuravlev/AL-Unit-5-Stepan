def insertion_sort(array):
    indexing_length = range(1, len(array))
    for i in indexing_length:
        value_to_sort = array[i]

        while array[i-1] > value_to_sort and i > 0:
            array[i], array[i-1] = array[i-1], array[i]  # two values can be swapped without temp in Python
            i -= 1

    return array

#test_arr = [5, 2, 8, 10, 1, 5,5,23, 45,1,2,2,2]
#print(insertion_sort(test_arr))
