# Author: Harsh Kohli
# Date created: 8/10/2020

def expressiveWords(S, words):
    s_len = len(S)
    count = 0
    for word in words:
        word_len = len(word)
        ptr1, ptr2 = 0, 0
        is_valid = True
        while True:
            len1, len2 = 1, 1
            if ptr1 >= word_len or ptr2 >=s_len or word[ptr1] != S[ptr2]:
                is_valid = False
                break
            while ptr1 < (word_len - 1) and word[ptr1] == word[ptr1 + 1]:
                ptr1 = ptr1 + 1
                len1 = len1 + 1
            while ptr2 < (s_len - 1) and S[ptr2] == S[ptr2 + 1]:
                ptr2 = ptr2 + 1
                len2 = len2 + 1
            if len2 == len1 or (len2 >= 3 and len1 < len2):
                if ptr1 == word_len - 1:
                    final_char = word[ptr1]
                    for index in range(ptr2, s_len):
                        s_char = S[index]
                        if s_char != final_char:
                            is_valid = False
                            break
                    break
                if ptr2 == s_len - 1:
                    is_valid = False
                    break
                ptr1 = ptr1 + 1
                ptr2 = ptr2 + 1
            else:
                is_valid = False
                break
        if is_valid:
            count = count + 1
    return count


S = ""
words =  ["hello", "hi", "helo"]
num_exp = expressiveWords(S, words)
print(num_exp)
