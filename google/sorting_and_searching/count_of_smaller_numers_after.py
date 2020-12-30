# Author: Harsh Kohli
# Date created: 10/16/2020

def countSmaller_suboptimal(nums):
    with_index = [(num, i) for i, num in enumerate(nums)]
    sorted_with_index = sorted(with_index)
    answer = [0 for _ in range(len(nums))]
    for num, pos in sorted_with_index:
        for index in range(pos - 1, -1, -1):
            if nums[index] > num:
                answer[index] = answer[index] + 1
    return answer


class Node():
    def __init__(self, val, index, smaller_after):
        self.val = val
        self.index = index
        self.left = None
        self.right = None
        self.smaller_after = smaller_after


def insert(root, index, num, path_sum):
    if num <= root.val:
        if root.left == None:
            smalls = Node(num, index, 0)
            root.left = smalls
            root.smaller_after = root.smaller_after + 1
            return path_sum
        else:
            smalls = insert(root.left, index, num, path_sum)
            root.smaller_after = root.smaller_after + 1
            return smalls

    else:
        if root.right == None:
            smalls = Node(num, index, 0)
            root.right = smalls
            return root.smaller_after + path_sum + 1
        else:
            smalls = insert(root.right, index, num, root.smaller_after + path_sum + 1)
            return smalls


def countSmaller(nums):
    if len(nums) == 0:
        return []
    root = Node(nums[-1], 0, 0)
    smaller_afters = []
    smaller_afters.append(0)
    for index in range(len(nums) - 2, -1, -1):
        num = nums[index]
        smalls = insert(root, index, num, 0)
        smaller_afters.append(smalls)
    smaller_afters.reverse()
    return smaller_afters


nums = [6, 2, 8, 1, 3, 9, 7, 5]
smaller_later = countSmaller(nums)
print(smaller_later)
