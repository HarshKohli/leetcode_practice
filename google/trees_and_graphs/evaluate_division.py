# Author: Harsh Kohli
# Date created: 10/2/2020

from queue import Queue

def dfs(a, adj_list, var_value_map):
    if a not in adj_list:
        return
    for dependent in adj_list[a]:
        b, value = dependent
        if b in var_value_map:
            continue
        a_val = var_value_map[a]
        b_val = a_val / value
        var_value_map[b] = b_val
        dfs(b, adj_list, var_value_map)


class Node:
    def __init__(self, next=None):
        self.next = next

def calcEquation(equations, values, queries):

    var_node_map = {}
    for equation, value in zip(equations, values):
        a, b = equation[0], equation[1]
        if a not in var_node_map:
            a_node = Node()
            var_node_map[a] = a_node
        else:
            a_node = var_node_map[a]
        if b not in var_node_map:
            b_node = Node()
            var_node_map[b] = b_node
        else:
            b_node = var_node_map[b]
        if a_node.next is None:
            a_node.next = [(b_node, value)]
        else:
            a_node.next.append((b_node, value))
        if b_node.next is None:
            b_node.next = [(a_node, float(1 / value))]
        else:
            b_node.next.append((a_node, float(1 / value)))

    answers = []
    for query in queries:
        a, b = query
        if a not in var_node_map or b not in var_node_map:
            answers.append(-1.0)
            continue
        q = Queue()
        a_node, b_node = var_node_map[a], var_node_map[b]
        q.put((a_node, 1.0))
        found = False
        seen = []
        while not q.empty():
            new_node, running_val = q.get()
            if new_node in seen:
                continue
            else:
                seen.append(new_node)
            if new_node == b_node:
                answers.append(running_val)
                found = True
                break
            else:
                if new_node.next is not None:
                    for child, val in new_node.next:
                        q.put((child, running_val*val))
        if not found:
            answers.append(-1.0)
    return answers






    # adj_list = {}
    # for equation, value in zip(equations, values):
    #     a, b = equation[0], equation[1]
    #     if a in adj_list:
    #         adj_list[a].append((b, value))
    #     else:
    #         adj_list[a] = [(b, value)]
    #     if b in adj_list:
    #         adj_list[b].append((a, float(1 / value)))
    #     else:
    #         adj_list[b] = [(a, float(1 / value))]
    #
    # for query in queries:
    #     a, b = query
    #     a_val = 1.0


    # var_value_map = {}
    # for a in adj_list:
    #     if a not in var_value_map:
    #         var_value_map[a] = 1.0
    #         dfs(a, adj_list, var_value_map)
    # answers = []
    # for query in queries:
    #     a, b = query
    #     if a not in var_value_map or b not in var_value_map:
    #         answers.append(-1.0)
    #     else:
    #         answers.append(var_value_map[a] / var_value_map[b])
    # return answers


equations = [["a","b"],["c","d"]]
values = [1.0,1.0]
queries = [["a","c"],["b","d"],["b","a"],["d","c"]]

solved = calcEquation(equations, values, queries)
print(solved)
