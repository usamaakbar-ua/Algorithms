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


def kmp_string_search(long: str, pattern: str) -> int:

    count = 0

    prefix_table = compute_prefix_table(pattern)

    i = 0
    j = 0

    while i < len(long):
        if long[i] == pattern[j]:
            i += 1
            j += 1

        if j == len(pattern):
            count += 1
            j = prefix_table[j -1]
        elif i < len(long) and long[i] != pattern[j]:
            if j != 0:
                j = prefix_table[j - 1]
            else:
                i += 1
    return count


def compute_prefix_table(pattern: str) -> list:
    prefix_table = [0] * len(pattern)
    j = 0

    for i in range(1, len(pattern)):
        if pattern[i] == pattern[j]:
            j += 1
            prefix_table[i] = j
        else:
            while j > 0 and pattern[i] != pattern[j]:
                j = prefix_table[j - 1]
            if pattern[i] == pattern[j]:
                j += 1
                prefix_table[i] = j
            else:
                prefix_table[i] = 0
    return prefix_table
