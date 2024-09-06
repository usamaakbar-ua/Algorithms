#Linear Search


def linear_search(arr, value):
    for i in range(len(arr)):
        if arr[i] == value:
            return i
    return -1


# Write a function naiveStringSearch that takes in two strings,
# long and pattern, and returns the number of occurrences of pattern in long.
# The function should use a naive string search algorithm to search for patterns in long.

def naive_string_search(long_str, pattern):
    count = 0
    long_len = len(long_str)
    pattern_len = len(pattern)

    for i in range(long_len - pattern_len + 1):
        for j in range(pattern_len):
            if pattern[j] != long_str[i + j]:
                break
            if j == pattern_len - 1:
                count += 1

    return count

