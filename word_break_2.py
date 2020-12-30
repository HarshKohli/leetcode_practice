# Author: Harsh Kohli
# Date created: 12/6/2020

import copy


def get_remaining_strings(index, sentences):
    remaining = set()
    for sentence in sentences:
        count = 0
        for ptr, x in enumerate(sentence):
            if x != ' ':
                count = count + 1
            if count == index:
                rem = sentence[ptr + 1:]
                remaining.add(rem)
    return remaining


def recurse(s, wordDict, index, words, part_word, size, remaining_dict):
    all_sentences = set()
    if index == size:
        if part_word in wordDict:
            words.append(part_word)
            sentence = ' '.join(words)
            all_sentences.add(sentence)
            return all_sentences
        else:
            return all_sentences
    letter = s[index]
    new_word = part_word + letter
    if new_word in wordDict:
        if index in remaining_dict:
            if len(remaining_dict[index]) != 0:
                so_far = ' '.join(words)
                for part in remaining_dict[index]:
                    rem_word = part.split(' ')[0]
                    next_word = part_word + rem_word
                    if next_word not in wordDict:
                        continue
                    new_sentence = so_far + ' ' + part_word + part
                    all_sentences.add(new_sentence.strip())
        else:
            words_copy = copy.deepcopy(words)
            words_copy.append(new_word)
            sentences1 = recurse(s, wordDict, index + 1, words_copy, '', size, remaining_dict)
            rem_strings = get_remaining_strings(index, sentences1)
            remaining_dict[index] = rem_strings
            for x in sentences1:
                all_sentences.add(x.strip())

    sentences2 = recurse(s, wordDict, index + 1, words, new_word, size, remaining_dict)
    for x in sentences2:
        all_sentences.add(x.strip())

    return all_sentences


def wordBreak(s, wordDict):
    words = set(wordDict)
    all_sentences = recurse(s, words, 0, [], '', len(s), {})
    return list(all_sentences)


s = "aaaaaaa"
wordDict = ['aaaa', 'aaa']
print(wordBreak(s, wordDict))
