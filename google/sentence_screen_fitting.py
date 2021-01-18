# Author: Harsh Kohli
# Date created: 1/16/2021

def get_next_col(col, next_word):
    return col + len(next_word)


def recurse(sentence, index, row_no, col_no, rows, cols, count):
    if index == len(sentence):
        count = count + 1
        index = 0
    if row_no == rows:
        return count
    next_word = sentence[index]
    next_col = get_next_col(col_no, next_word)
    if next_col > cols:
        return recurse(sentence, index, row_no + 1, 0, rows, cols, count)
    else:
        return recurse(sentence, index + 1, row_no, next_col + 1, rows, cols, count)


def wordsTyping(sentence, rows, cols):
    #count = recurse(sentence, 0, 0, 0, rows, cols, 0)

    dp = {}
    col_no, index, count = 0, 0, 0
    for _ in range(rows):
        if index in dp:
            next_index, small_count = dp[index]
            index = next_index
            count = small_count + count
            continue
        small_count = 0
        init_index = index
        while col_no <= cols:
            next_word = sentence[index]
            next_col = col_no + len(next_word)
            if next_col > cols:
                break
            else:
                index = index + 1
                if index == len(sentence):
                    small_count = small_count + 1
                    count = count + 1
                    index = 0
                col_no = next_col + 1
        dp[init_index] = (index, small_count)
        col_no = 0
    return count


rows = 10000
cols = 10000
sentence = ["a"]
print(wordsTyping(sentence, rows, cols))
