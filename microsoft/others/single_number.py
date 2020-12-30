# Author: Harsh Kohli
# Date created: 11/23/2020

def singleNumber(nums):
    answer = 0
    for num in nums:
        answer = answer ^ num
    return answer


