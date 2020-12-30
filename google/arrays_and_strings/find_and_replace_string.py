# Author: Harsh Kohli
# Date created: 8/11/2020

def findReplaceString(S, indexes, sources, targets):
    final_string = ""
    ptr = 0
    slen = len(S)
    rep_dict = {}
    for index, source, target in zip(indexes, sources, targets):
        rep_dict[index] = {'source': source, 'target': target}

    while ptr < slen:
        if ptr in rep_dict:
            source, target = rep_dict[ptr]['source'], rep_dict[ptr]['target']
            size = len(source)
            if ptr + size > len(S):
                final_string = final_string + S[ptr]
                ptr = ptr + 1
                continue
            else:
                compare_with = S[ptr: ptr + size]
                if source == compare_with:
                    final_string = final_string + target
                    ptr = ptr + size
                    continue
                else:
                    final_string = final_string + S[ptr]
                    ptr = ptr + 1
                    continue
        else:
            final_string = final_string + S[ptr]
            ptr = ptr + 1
            continue
    return final_string


S = "abcd"
indexes = [0, 2]
sources = ["a", "cd"]
targets = ["eee", "ffff"]
answer = findReplaceString(S, indexes, sources, targets)
print(answer)
