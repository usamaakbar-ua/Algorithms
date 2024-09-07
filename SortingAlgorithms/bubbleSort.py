def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                #Swap Elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


print(bubble_sort([10, 2, 15, 20, 4, 5, 1, 8, 9, ]))
