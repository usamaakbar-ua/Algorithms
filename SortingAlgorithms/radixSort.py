def radixSort(arr):
    maxNum = max(arr)
    maxLength = len(str(maxNum))

    for i in range(maxLength):
        buckets = [[] for _ in range[10]]

        for num in arr:
            digit = getDigit(num, i)
            buckets[digit].append(num)

        arr = [num for bucket in buckets for num in bucket]

    return arr


def getDigit(num, place):
    return (abs(num) // 10 ** place) % 10


print(radixSort([10, 5, 2, 8, 6, 3, 1, 9]))
