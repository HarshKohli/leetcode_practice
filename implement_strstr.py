# Author: Harsh Kohli
# Date created: 11/7/2020

def strStr(haystack, needle):
    size, needle_size = len(haystack), len(needle)
    if needle_size == 0:
        return 0
    if size == 0:
        return -1
    if needle_size > size:
        return -1

    all_strings = {}

    for index in range(0, size - needle_size + 1):
        window = haystack[index: index + needle_size]
        if window not in all_strings:
            all_strings[window] = index

    if needle in all_strings:
        return all_strings[needle]
    return -1


haystack = "aaaaa"
needle = "aaa"
print(strStr(haystack, needle))
