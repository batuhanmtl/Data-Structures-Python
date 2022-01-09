def h(k, i):
    return (k % 10 + i) % 10


def push(arr, b):
    for i in range(10):
        if arr[h(b, i)] == -1:
            c = h(b, i)
            arr[c] = b
            return c


def main():
    arr = []

    for i in range(10):
        arr.append(-1)

    print(arr)
    push(arr, 72)
    print(arr)
    push(arr, 27)
    print(arr)
    push(arr, 36)
    print(arr)
    push(arr, 24)
    print(arr)
    push(arr, 63)
    print(arr)
    push(arr, 81)
    print(arr)
    push(arr, 92)
    print(arr)
    push(arr, 91)
    print(arr)


main()
