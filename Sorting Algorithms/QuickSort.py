def partition(arr, first, last):
    # pivot value = first value
    pivotvalue = arr[first]

    left = first + 1
    right = last

    done = False

    while not done:
        while left <= right and arr[left] <= pivotvalue:
            left = left + 1
        while arr[right] >= pivotvalue and right >= left:
            right = right - 1

        if right < left:
            done = True
        else:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
    temp = arr[first]
    arr[first] = arr[right]
    arr[right] = temp
    return right


def quick_sort_recursion(arr, first, last):
    if first < last:
        splitpoint = partition(arr, first, last)

        # left right
        quick_sort_recursion(arr, first, splitpoint - 1)
        quick_sort_recursion(arr, splitpoint + 1, last)


def quick_sort(arr):
    quick_sort_recursion(arr, 0, len(arr) - 1)
    return arr


arr = [3, 2, 13, 4, 6, 5, 73, 4]
quick_sort(arr)
print(arr)
