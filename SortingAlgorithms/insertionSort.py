def insertionSort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current
    return arr


print(insertionSort([5, 2, 8, 6, 11, 45, 8, 4, 1, 0]))
