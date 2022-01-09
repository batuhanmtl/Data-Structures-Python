def selectionSort(arr):
    """
    selection sort
    """
    for i in range(len(arr) - 1, 0, -1):
        positionOfmax = 0

        for location in range(1, i + 1):
            if arr[location] > arr[positionOfmax]:
                positionOfmax = location
            temp = arr[i]
            arr[i] = arr[positionOfmax]
            arr[positionOfmax] = temp
    return arr


arr = [3, 2, 13, 4, 6, 5, 7, 8, 1, 20]
print("Unsorted arr :")
print(arr)
selectionSort(arr)
print("Sorted arr :")
print(arr)
