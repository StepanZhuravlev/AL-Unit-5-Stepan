# Evaluation: most efficient search algorithm covered in the course

def binary_search(array, search, left, right):
    mid = round(left + ((right-left) / 2))
    if right < left:
        return -1
    else:
        if array[mid] < search:
            return binary_search(array, search, mid+1, right)
        elif array[mid] < search:
            return binary_search(array, search, left, mid-1)
        else:
            return mid


#test_arr = [1, 2, 6, 10, 25, 70, 73, 450]
#print(binary_search(test_arr, 8, 1, len(test_arr)))
