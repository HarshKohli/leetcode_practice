# Author: Harsh Kohli
# Date created: 10/9/2020

import copy


def is_valid(square, size):
    for index in range(size):
        word = square[index]
        word_vert = ''
        for x in range(size):
            word_vert = word_vert + square[x][index]
        if word_vert != word:
            return False
    return True


def recurse(square, all_words, current_word, size, prefix_dict):
    square.append(current_word)
    cur_size = len(square)
    if len(square) == size:
        if is_valid(square, size):
            valid_square = copy.deepcopy(square)
            square.pop()
            return [valid_square]
        else:
            square.pop()
            return []
    valid_squares = []
    prefix = ''
    for row in range(cur_size):
        prefix = prefix + square[row][cur_size]
    if prefix in prefix_dict:
        for word in prefix_dict[prefix]:
            if len(word) == size:
                squares = recurse(square, all_words, word, size, prefix_dict)
                valid_squares.extend(copy.deepcopy(squares))
    square.pop()
    return valid_squares


def wordSquares(words):
    valid_squares = []
    prefix_dict = {}
    for word in words:
        for index in range(1, len(word)):
            pre = word[:index]
            if pre in prefix_dict:
                prefix_dict[pre].append(word)
            else:
                prefix_dict[pre] = [word]

    for word in words:
        valid_squares.extend(recurse([], words, word, len(word), prefix_dict))
    return valid_squares


words = ["area","lead","wall","lady","ball"]
squares = wordSquares(words)
print(squares)
