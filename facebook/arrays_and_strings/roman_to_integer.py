# Author: Harsh Kohli
# Date created: 10/20/2020

def romanToInt(s):
    symbol_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    double_symbol_map = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    skip = False
    final_num = 0
    for index, x in enumerate(s):
        if skip:
            skip = False
            continue
        if index < len(s) - 1:
            two = s[index: index + 2]
            if two in double_symbol_map:
                final_num = final_num + double_symbol_map[two]
                skip = True
                continue
        final_num = final_num + symbol_map[x]

    return final_num


s = "MCMXCIV"
print(romanToInt(s))
