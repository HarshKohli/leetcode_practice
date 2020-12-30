# Author: Harsh Kohli
# Date created: 12/2/2020

def groupStrings(strings):
    combinations_map = {}
    for word in strings:
        if word not in combinations_map:
            new_arr = [word]
            for rot in range(1, 27):
                new_word = ''
                for x in word:
                    num = ord(x)
                    new_num = (num - 97 + rot) % 26 + 97
                    new_word = new_word + chr(new_num)
                combinations_map[new_word] = new_arr
        else:
            combinations_map[word].append(word)

    answers = []
    for key, comb in combinations_map.items():
        if len(comb) > 0 and comb not in answers:
            answers.append(comb)

    return answers


# strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
strings = ["a", "a"]
print(groupStrings(strings))
