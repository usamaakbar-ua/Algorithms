def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
            #Swap Elements

            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr


print(selection_sort([5, 2, 4, 8, 12, 46, 0]))
