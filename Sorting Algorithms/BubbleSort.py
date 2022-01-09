def bubbleSort(arr):
    '''
    bubble sort
    '''

    for n in range(len(arr)-1,0,-1):
        for k in range(n):
            if arr[k] > arr[k+1]:
                temp =arr[k]
                arr[k] = arr[k+1]
                arr[k+1]=temp
    return arr

arr = [20,2,54,21,10,9,89,34]
print("Unsorted arr :")
print(arr)
arr = bubbleSort(arr)
print("Sorted arr :")
print(arr)
