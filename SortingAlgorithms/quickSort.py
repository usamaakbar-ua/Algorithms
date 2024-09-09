def quickSort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    if left < right:
        pivotIndex = partition(arr, left, right)
        quickSort(arr, left, pivotIndex - 1)
        quickSort(arr, pivotIndex + 1, right)

    return arr


def partition(arr, left, right):
    pivot = arr[right]
    i = left
    for j in range(left, right):
        if arr[j] < pivot:
            #Swap elements
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    #Swap pivot into correct position
    arr[i], arr[right] = arr[right], arr[i]
    return i


print(quickSort([4, 8, 6, 7, 2, 1, 99, 3, 44, 88, 102, 1]))
