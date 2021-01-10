# Author: Harsh Kohli
# Date created: 1/11/2021

def get_level(element):
    count = 0
    for x in element:
        if x == '\t':
            count = count + 1
        else:
            break
    return count


def get_paths(element, path_so_far, all_parts, index):
    present_level = get_level(element)
    if '.' in element:
        return [path_so_far + '/' + element[present_level:]]
    all_paths = []
    for next_index in range(index + 1, len(all_parts)):
        next_element = all_parts[next_index]
        next_level = get_level(next_element)
        if next_level == present_level + 1:
            new_path = path_so_far + '/' + element[present_level:]
            all_paths.extend(get_paths(next_element, new_path, all_parts, next_index))
        elif next_level <= present_level:
            break
    return all_paths


def lengthLongestPath(input):
    if len(input) == 0:
        return 0
    all_parts = input.split('\n')
    all_paths = []
    for index, part in enumerate(all_parts):
        level = get_level(part)
        if level == 0:
            all_paths.extend(get_paths(part, '', all_parts, index))
    print(all_paths)
    max_len = 0
    for path in all_paths:
        if len(path) - 1 > max_len:
            max_len = len(path) - 1
    return max_len


s = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
print(lengthLongestPath(s))
