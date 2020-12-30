# Author: Harsh Kohli
# Date created: 10/18/2020

def candy(ratings):
    if len(ratings) == 0:
        return 0
    min_rating = float('inf')
    for rating in ratings:
        if rating < min_rating:
            min_rating = rating
    candies = []
    for rating in ratings:
        candies.append(rating - min_rating + 1)
    while True:
        did_change = False
        for index, rating in enumerate(ratings):
            candy = candies[index]
            left, left_candy = 0, 0
            if index != 0:
                left = ratings[index - 1]
                left_candy = candies[index - 1]
            right, right_candy = 0, 0
            if index != len(ratings) - 1:
                right = ratings[index + 1]
                right_candy = candies[index + 1]
            if rating > left and rating > right:
                right_amount = max(left_candy, right_candy) + 1
            elif rating > left:
                right_amount = left_candy + 1
            elif rating > right:
                right_amount = right_candy + 1
            else:
                right_amount = 1
            if right_amount != candy:
                candies[index] = right_amount
                did_change = True
                continue
        if not did_change:
            break

    num_candies = 0
    for candy in candies:
        num_candies = num_candies + candy
    return num_candies


ratings = [1,3,2,2,1]
print(candy(ratings))
