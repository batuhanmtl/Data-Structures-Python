def insertionSort(arr):
    """
    insertion sort
    """

    for i in range(1, len(arr)):

        currentvalue = arr[i]

        position = i
        # sublist
        while position > 0 and arr[position - 1] > currentvalue:
            arr[position] = arr[position - 1]
            position -= 1

        arr[position] = currentvalue
    return arr


arr = [3, 2, 13, 4, 6, 5, 7, 8, 1, 20]
print("Unsorted arr :")
print(arr)
insertionSort(arr)
print("Sorted arr :")
print(arr)
