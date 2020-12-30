# Author: Harsh Kohli
# Date created: 10/19/2020

def getHint(secret, guess):
    count_map = {}
    for x in secret:
        if x in count_map:
            count_map[x] = count_map[x] + 1
        else:
            count_map[x] = 1
    bulls = 0
    are_bulls = [0 for _ in range(len(secret))]
    for index, (x, y) in enumerate(zip(secret, guess)):
        if x == y:
            bulls = bulls + 1
            count_map[x] = count_map[x] - 1
            are_bulls[index] = 1
    cows = 0
    for x, is_bull in zip(guess, are_bulls):
        if is_bull:
            continue
        if x in count_map and count_map[x] != 0:
            cows = cows + 1
            count_map[x] = count_map[x] - 1

    hint = str(bulls) + 'A' + str(cows) + 'B'
    return hint


secret = "11"
guess = "10"
hint = getHint(secret, guess)
print(hint)
