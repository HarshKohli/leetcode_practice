# Author: Harsh Kohli
# Date created: 7/24/2020

def totalFruit(tree):

    if len(tree) > 0:
        types, toggle, prev, start, max = [tree[0]], 0, tree[0], 0, 0

        for p, num in enumerate(tree[1:]):
            index = p + 1
            if num in types or len(types) < 2:
                if prev != num:
                    toggle = index
                if num not in types:
                    types.append(num)
                prev = num
                continue
            elif num not in types and len(types) == 2:
                num_fruit = index - start
                start = toggle
                types = [num]
                types.append(prev)
                if num_fruit > max:
                    max = num_fruit
                toggle = index
                prev = num

        num_fruit = len(tree) - start
        if num_fruit > max:
            max = num_fruit
        return max

    else:
        return 0


input = [1,0,3,4,3]
num_fruit = totalFruit(input)
print(num_fruit)
