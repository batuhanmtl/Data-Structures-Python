def counting_sort(arr, maxval):
    """
    count sort
    """
    n = len(arr)
    m = maxval + 1
    count = [0] * m  # [0,0,0,...,0]

    for a in arr:
        count[a] += 1
    i = 0
    for a in range(m):
        for c in range(count[a]):
            arr[i] = a
            i += 1
    return arr


List = [1, 2, 3, 4, 5, 6, 7, 7, 7, 1, 1, 1, 2, 3]
counting_sort(List, 7)
print(List)
